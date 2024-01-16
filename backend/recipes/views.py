from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics, views, permissions, status

from .models import Recipe, RecipeIngredient, UnitConversion
from .serializers import RecipeSerializer


class RecipeAPIView(generics.ListAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer

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
