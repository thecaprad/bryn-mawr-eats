# Generated by Django 4.1.5 on 2024-01-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_unitconversion_init'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientunit',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
