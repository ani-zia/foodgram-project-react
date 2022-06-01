from django.contrib import admin

from .models import Recipe


class IngredientForRecipeInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    list_display_links = ('name',)
    list_filter = ('name', 'author', 'tags')
    inlines = (IngredientForRecipeInLine, )
    readonly_fields = ('is_favorited',)

    @admin.display(description='В избранном')
    def is_favorited(self, instance):
        return instance.fav_recipe.count()


admin.site.register(Recipe, RecipeAdmin)
