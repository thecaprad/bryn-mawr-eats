from django.db import models

class GroceryAisle(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, unique=True)

  def __str__(self):
    return self.name

class IngredientUnit(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, unique=True)

  def __str__(self):
    return self.name

class GroceryItem(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, unique=True)
  grocery_aisle = models.ForeignKey(GroceryAisle, blank=True, null=True, on_delete=models.SET_NULL)

  @property
  def grocery_aisle_name(self):
     return self.grocery_aisle.name

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']

class Recipe(models.Model):
  name = models.CharField(max_length=250, blank=False, null=False, unique=True)
  prep_time = models.IntegerField(blank=True, null=True)
  cook_time = models.IntegerField(blank=True, null=True)
  source_url = models.URLField(blank=True, null=True)
  image_url = models.URLField(blank=True, null=True)

  def __str__(self):
    return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, blank=False, null=False, on_delete=models.CASCADE, related_name='recipe_ingredients')
    grocery_item = models.ForeignKey(GroceryItem, blank=False, null=False, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=False, null=False, default=1)
    unit = models.ForeignKey(IngredientUnit, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.recipe} — {self.grocery_item}"

    def save(self, *args, **kwargs):
        if not self.id and not self.unit:
            whole = IngredientUnit.objects.get_or_create(name='whole')
            self.unit = whole
        return super(RecipeIngredient, self).save(*args, **kwargs)

class UnitConversion(models.Model):
    bigger_unit = models.ForeignKey(IngredientUnit, on_delete=models.CASCADE, related_name='bigger_unit')
    smaller_unit = models.ForeignKey(IngredientUnit, on_delete=models.CASCADE, related_name='smaller_unit')
    conversion_factor = models.FloatField(blank=False, null=False, default=1)

    def __str__(self):
      return f'{self.bigger_unit.name} —> {self.smaller_unit.name} (conversion factor: {self.conversion_factor})'
