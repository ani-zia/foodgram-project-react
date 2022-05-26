from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)

from apps.ingredients.urls import ingredients_router
from apps.recipes.urls import recipes_router
from apps.tags.urls import tags_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Путь для Redoc:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Путь для спеки от Swagger — тут можно делать запросы как в Postman!
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/ingredients/', include(ingredients_router.urls)),
    path('api/tags/', include(tags_router.urls)),
    path('api/recipes/', include(recipes_router.urls)),
    path('api/', include('apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
