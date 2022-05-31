from apps.ingredients.urls import ingredients_router
from apps.recipes.urls import recipes_router
from apps.tags.urls import tags_router
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/ingredients/', include(ingredients_router.urls)),
    path('api/tags/', include(tags_router.urls)),
    path('api/recipes/', include(recipes_router.urls)),
    path('api/', include('apps.users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
