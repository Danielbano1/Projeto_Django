# Generated by Django 5.0.2 on 2024-03-20 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='serving',
            new_name='servings',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='serving_unit',
            new_name='servings_unit',
        ),
    ]
