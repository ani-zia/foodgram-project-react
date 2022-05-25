from rest_framework.filters import SearchFilter


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'
