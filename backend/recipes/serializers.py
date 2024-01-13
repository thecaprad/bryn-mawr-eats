from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = ('id', 'name', 'prep_time', 'cook_time', 'source_url', 'image_url')