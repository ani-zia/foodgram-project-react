from rest_framework import serializers

from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Ingredient
