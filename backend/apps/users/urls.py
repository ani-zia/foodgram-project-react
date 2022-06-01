from django.urls import include, path

from .views import FollowApiView, FollowListViewSet

urlpatterns = [
    path(
        'users/subscriptions/',
        FollowListViewSet.as_view(),
        name='subscriptions'),
    path(
        'users/<int:pk>/subscribe/',
        FollowApiView.as_view(),
        name='subscribe'),
    path('', include("djoser.urls")),
    path('auth/', include('djoser.urls.authtoken')),
]
