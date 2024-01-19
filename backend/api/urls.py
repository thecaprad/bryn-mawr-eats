from django.urls import path, re_path
from recipes.views import RecipeAPIView, GroceryItemAPIView, GroceryListView, UnitConversionView, IngredientUnitAPIView, AisleAPIView

urlpatterns = [
  path('recipes/', RecipeAPIView.as_view(), name='recipe_list'),
  re_path('^grocery-list/(?P<recipe_ids>[\d|,]+)/?', GroceryListView.as_view(), name='grocery_list'),
  path('units/', UnitConversionView.as_view(), name='units'),
  path('grocery-items/', GroceryItemAPIView.as_view(), name='grocery_items'),
  path('ingredient-units/', IngredientUnitAPIView.as_view(), name="ingredient_units"),
  path('aisles/', AisleAPIView.as_view(), name="aisles"),
]