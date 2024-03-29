from django.contrib import admin

from .models import GroceryAisle, IngredientUnit, GroceryItem, Recipe, RecipeIngredient, UnitConversion


class GroceryAisleAdmin(admin.ModelAdmin):
  list_display = (
    "name",
  )

admin.site.register(GroceryAisle, GroceryAisleAdmin)

class IngredientUnitAdmin(admin.ModelAdmin):
  list_display = (
    "name",
  )

admin.site.register(IngredientUnit, IngredientUnitAdmin)

class GroceryItemAdmin(admin.ModelAdmin):
  list_display = (
    "name",
    "grocery_aisle"
  )

admin.site.register(GroceryItem, GroceryItemAdmin)

class RecipeIngredientInline(admin.TabularInline):
  model = RecipeIngredient
  fields = ['grocery_item', 'quantity', 'unit']

class RecipeAdmin(admin.ModelAdmin):
  inlines = [RecipeIngredientInline]
  list_display = (
    "name",
    "prep_time",
    "cook_time",
    "source_url",
    "image_url"
  )

admin.site.register(Recipe, RecipeAdmin)

class RecipeIngredientAdmin(admin.ModelAdmin):
  list_display = (
    "recipe",
    "grocery_item",
    "quantity",
    "unit"
  )

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

class UnitConversionAdmin(admin.ModelAdmin):
  pass

admin.site.register(UnitConversion, UnitConversionAdmin)
