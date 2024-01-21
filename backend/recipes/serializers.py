from rest_framework import serializers

from .models import Recipe, RecipeIngredient, GroceryItem, IngredientUnit, GroceryAisle

class GroceryAisleSerializer(serializers.ModelSerializer):
  class Meta:
    model = GroceryAisle
    fields = ('id', 'name')

class GroceryItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = GroceryItem
    fields = ('id', 'name', 'grocery_aisle_name')

class IngredientUnitSerializer(serializers.ModelSerializer):
  class Meta:
    model = IngredientUnit
    fields = ('id', 'name')

class RecipeIngredientSerializer(serializers.ModelSerializer):
  grocery_item_name = serializers.ReadOnlyField()
  unit_name = serializers.ReadOnlyField()
  class Meta:
    model = RecipeIngredient
    fields = ('grocery_item', 'grocery_item_name', 'quantity', 'unit', 'unit_name')

class RecipeSerializer(serializers.ModelSerializer):
  recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)
  class Meta:
    model = Recipe
    fields = ('id', 'name', 'prep_time', 'cook_time', 'source_url', 'image_url', 'recipe_ingredients')