# Generated by Django 4.1.5 on 2024-01-15 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipeingredient_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitConversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversion_factor', models.FloatField(default=1)),
                ('bigger_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bigger_unit', to='recipes.ingredientunit')),
                ('smaller_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smaller_unit', to='recipes.ingredientunit')),
            ],
        ),
    ]