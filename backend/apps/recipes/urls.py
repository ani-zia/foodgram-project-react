from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet

recipes_router = DefaultRouter()
recipes_router.register('', RecipeViewSet)
