# Generated by Django 4.1.5 on 2024-01-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_add_unique_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='grocery_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.groceryitem'),
        ),
    ]
