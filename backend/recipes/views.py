from django.http import JsonResponse
from rest_framework import generics, views, permissions, status

from .models import Recipe, RecipeIngredient
from .serializers import RecipeSerializer


class RecipeAPIView(generics.ListAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer

class GroceryListView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, recipe_ids):
        recipe_ids = recipe_ids.split(',')
        recipe_ingredients = {}
        aisles = []
        for r_id in recipe_ids:
            try:
                for ri in RecipeIngredient.objects.filter(recipe_id=int(r_id)):
                    # Handle unique aisles
                    if ri.grocery_item.grocery_aisle.name not in aisles:
                        aisles.append(ri.grocery_item.grocery_aisle.name)

                    # Handle ingredients
                    recipe_ingredients[ri.id] = {
                        "id": ri.grocery_item.id,
                        "grocery_aisle": ri.grocery_item.grocery_aisle.name,
                        "name": ri.grocery_item.name,
                        "quantity": ri.quantity,
                        "unit": ri.unit.name if ri.unit else ''
                    }
            except Exception:
                pass
        return JsonResponse({"recipe_ids": recipe_ids, "recipe_ingredients": recipe_ingredients, "aisles": aisles})
