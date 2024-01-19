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

class RecipeIngredeintSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecipeIngredient
    fields = ('grocery_item', 'quantity', 'unit')

class RecipeSerializer(serializers.ModelSerializer):
  # ingredients = RecipeIngredeintSerializer(many=True, read_only=True)
  class Meta:
    model = Recipe
    fields = ('id', 'name', 'prep_time', 'cook_time', 'source_url', 'image_url')