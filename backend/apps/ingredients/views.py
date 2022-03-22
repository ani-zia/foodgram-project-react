from rest_framework import  filters, viewsets
from rest_framework.permissions import AllowAny

from .models import Ingredient
from .serializers import IngredientSerializer

class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    queryset = Ingredient.objects.all()
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
