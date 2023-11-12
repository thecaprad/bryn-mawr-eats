from django.db import models

class GroceryAisle(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, unique=True)

  def __str__(self):
    return self.name

class IngredientUnit(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)

  def __str__(self):
    return self.name

class GroceryItem(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)
  grocery_aisle = models.ForeignKey(GroceryAisle, blank=True, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']

class Recipe(models.Model):
  name = models.CharField(max_length=250, blank=False, null=False)
  prep_time = models.IntegerField(blank=True, null=True)
  cook_time = models.IntegerField(blank=True, null=True)
  source_url = models.URLField(blank=True, null=True)
  image_url = models.URLField(blank=True, null=True)

  def __str__(self):
    return self.name

class RecipeIngredient(models.Model):
  recipe = models.ForeignKey(Recipe, blank=False, null=False, on_delete=models.CASCADE)
  grocery_item = models.ForeignKey(GroceryItem, blank=False, null=False, on_delete=models.CASCADE)
  quantity = models.FloatField(blank=False, null=False, default=1)
  unit = models.ForeignKey(IngredientUnit, blank=True, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"{self.recipe} — {self.grocery_item}"
