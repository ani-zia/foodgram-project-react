from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

from .models import Tag
from .serializers import TagSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    queryset = Tag.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
