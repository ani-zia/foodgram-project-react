from django.contrib import admin

from .models import Recipe


class IngredientForRecipeInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    list_filter = ('name', 'author', 'tags')
    inlines = (IngredientForRecipeInLine, )


admin.site.register(Recipe, RecipeAdmin)
