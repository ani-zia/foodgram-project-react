from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .filters import IngredientSearchFilter
from .models import Ingredient
from .serializers import IngredientSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    queryset = Ingredient.objects.all()
    pagination_class = None
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)
