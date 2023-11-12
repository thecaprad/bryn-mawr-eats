from django.urls import path
from recipes.views import RecipeAPIView

urlpatterns = [
  path('recipes/', RecipeAPIView.as_view(), name='recipe_list'),
]