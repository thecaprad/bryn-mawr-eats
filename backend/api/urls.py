from django.urls import path, re_path
from recipes.views import RecipeAPIView, GroceryListView, UnitConversionView

urlpatterns = [
  path('recipes/', RecipeAPIView.as_view(), name='recipe_list'),
  re_path('^grocery-list/(?P<recipe_ids>[\d|,]+)/?', GroceryListView.as_view(), name='grocery_list'),
  path('units/', UnitConversionView.as_view(), name='units')
]