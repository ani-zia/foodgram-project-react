from rest_framework.routers import DefaultRouter

from .views import TagViewSet

tags_router = DefaultRouter()
tags_router.register('', TagViewSet)
