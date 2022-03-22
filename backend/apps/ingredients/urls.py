from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet

ingredients_router = DefaultRouter()
ingredients_router.register('', IngredientViewSet)
