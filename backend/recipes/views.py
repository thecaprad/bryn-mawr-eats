from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, views, permissions, status

from .models import Recipe, RecipeIngredient, UnitConversion, IngredientUnit, GroceryItem, GroceryAisle
from .serializers import RecipeSerializer, GroceryItemSerializer, IngredientUnitSerializer, GroceryAisleSerializer


class RecipeAPIView(generics.ListAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer

class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class GroceryItemAPIView(generics.ListAPIView):
    queryset = GroceryItem.objects.all().order_by('name')
    serializer_class = GroceryItemSerializer

    def post(self, request):
        new_item_name = request.data.get('new_item_name', None)
        grocery_aisle_id = request.data.get('grocery_aisle_id', None)
        if new_item_name and grocery_aisle_id:
            try:
                aisle = GroceryItem.objects.create(name=new_item_name, grocery_aisle_id=grocery_aisle_id)
                serialized_item = GroceryItemSerializer(aisle)
                return JsonResponse(serialized_item.data)
            except Exception:
                return Response(
                    {"error": "Cannot add item"},
                    status=status.HTTP_400_BAD_REQUEST
                )


class IngredientUnitAPIView(generics.ListAPIView):
    queryset = IngredientUnit.objects.all().order_by('name')
    serializer_class = IngredientUnitSerializer

    def post(self, request):
        new_unit_name = request.data.get('new_unit_name', None)
        if new_unit_name:
            try:
                new_unit_name = new_unit_name.lower()
                unit = IngredientUnit.objects.create(name=new_unit_name)
                serialized_unit = IngredientUnitSerializer(unit)
                return JsonResponse(serialized_unit.data)
            except Exception:
                return Response(
                    {"error": "Unit already exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )


class AisleAPIView(generics.ListAPIView):
    queryset = GroceryAisle.objects.all().order_by('name')
    serializer_class = GroceryAisleSerializer

    def post(self, request):
        new_aisle_name = request.data.get('new_aisle_name', None)
        if new_aisle_name:
            try:
                new_aisle_name = new_aisle_name.title()
                aisle = GroceryAisle.objects.create(name=new_aisle_name)
                serialized_aisle = GroceryAisleSerializer(aisle)
                return JsonResponse(serialized_aisle.data)
            except Exception:
                return Response(
                    {"error": "Aisle already exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )

class GroceryListView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, recipe_ids):
        recipe_ids = recipe_ids.split(',')
        ingredients = {}
        aisles = []
        for r_id in recipe_ids:
            for ri in RecipeIngredient.objects.filter(recipe_id=int(r_id)):
                # Handle unique aisles
                if ri.grocery_item.grocery_aisle.name not in aisles:
                    aisles.append(ri.grocery_item.grocery_aisle.name)

                # Handle ingredients
                if ri.grocery_item.id in ingredients:
                    existing_ingredient = ingredients[ri.grocery_item.id]

                    if existing_ingredient['unit'] != ri.unit.name:
                        if UnitConversion.objects.filter(bigger_unit__name=existing_ingredient['unit'], smaller_unit__name=ri.unit.name).exists():
                            conversion = UnitConversion.objects.get(bigger_unit__name=existing_ingredient['unit'], smaller_unit__name=ri.unit.name)
                            ingredients[ri.grocery_item.id]['unit'] = conversion.bigger_unit.name
                            ingredients[ri.grocery_item.id]['quantity'] = existing_ingredient['quantity'] + (conversion.conversion_factor * ri.quantity)
                        elif UnitConversion.objects.filter(bigger_unit__name=ri.unit.name, smaller_unit__name=existing_ingredient['unit']).exists():
                            conversion = UnitConversion.objects.get(bigger_unit__name=ri.unit.name, smaller_unit__name=existing_ingredient['unit'])
                            ingredients[ri.grocery_item.id]['unit'] = conversion.bigger_unit.name
                            ingredients[ri.grocery_item.id]['quantity'] = ri.quantity + (conversion.conversion_factor * existing_ingredient['quantity'])
                        else:
                            return JsonResponse({"need_conversion": [existing_ingredient['unit'], ri.unit.name]})
                    else:
                        ingredients[ri.grocery_item.id]['quantity'] += ri.quantity
                else:
                    ingredients[ri.grocery_item.id] = {
                        "id": ri.grocery_item.id,
                        "grocery_aisle": ri.grocery_item.grocery_aisle.name,
                        "name": ri.grocery_item.name,
                        "quantity": ri.quantity,
                        "unit": ri.unit.name if ri.unit else ''
                    }
        return JsonResponse({"recipe_ids": recipe_ids, "ingredients": ingredients, "aisles": aisles})

class UnitConversionView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        bigger_unit = request.data.get('bigger_unit', None)
        smaller_unit = request.data.get('smaller_unit', None)
        conversion_factor = request.data.get('conversion_factor', None)

        bigger_unit = IngredientUnit.objects.get(name=bigger_unit)
        smaller_unit = IngredientUnit.objects.get(name=smaller_unit)

        created = UnitConversion.objects.create(
            bigger_unit=bigger_unit,
            smaller_unit=smaller_unit,
            conversion_factor=conversion_factor
        )

        if created:
            return Response(
                status=status.HTTP_201_CREATED
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )
