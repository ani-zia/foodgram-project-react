from apps.ingredients.models import Ingredient
from apps.tags.models import Tag

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


User = get_user_model()

class Recipe(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientForRecipe',
        through_fields=('recipe', 'ingredient'),
        verbose_name='Ingredients'
        )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Tag',
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Author',
        )
    name = models.CharField(max_length=200, verbose_name='Title')
    image = models.ImageField(
        upload_to='recipes/', verbose_name='Image')
    text = models.TextField(verbose_name='Description')
    cooking_time = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Cooking time'
        )

    class Meta:
        ordering = ['-id',]
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class IngredientForRecipe(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Recipe'
        )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ingredient'
        )
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], 
        verbose_name='Amount'
        )

    class Meta:
        ordering = ['id',]
        verbose_name = 'Ingredient in Recipe'
        verbose_name_plural = 'Ingredients in Recipe'
        def __str__(self):
            return f'{self.recipe} - {self.ingredient}, {self.amount}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='fav_recipe',
        verbose_name='Recipe in fav'
    )

    class Meta:
        ordering = ['-id',]
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe'), name='unique_fav_recipe'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.recipe}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart_recipe',
        verbose_name='User',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart_recipe',
        verbose_name='Recipe',
    )

    class Meta:
        ordering = ['id',]
        verbose_name = 'Shoping Cart'
        verbose_name_plural = 'Shoping Carts'
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe'), name='unique_shop_cart'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.recipe}'
