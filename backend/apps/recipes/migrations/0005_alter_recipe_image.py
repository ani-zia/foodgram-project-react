# Generated by Django 4.0.3 on 2022-05-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='../media/recipe/', verbose_name='Image'),
        ),
    ]