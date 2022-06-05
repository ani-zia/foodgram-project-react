from apps.recipes.models import Recipe
from django.core.paginator import Paginator
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import Follow, User


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'username', 'first_name', 'last_name', 'password',
        )


class CustomUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name',
            'is_subscribed',
        )

    def get_is_subscribed(self, obj):
        request = self.context.get('request', )
        if not request or request.user.is_anonymous:
            return False
        return Follow.objects.filter(user=request.user,
                                     following=obj).exists()


class RecipeForFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class ListFollowSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')
    id = serializers.ReadOnlyField(source='following.id')
    username = serializers.ReadOnlyField(source='following.username')
    first_name = serializers.ReadOnlyField(source='following.first_name')
    last_name = serializers.ReadOnlyField(source='following.last_name')
    is_subscribed = serializers.SerializerMethodField('get_is_subscribed')
    recipes = serializers.SerializerMethodField('get_recipes')
    recipes_count = serializers.SerializerMethodField('get_recipes_count')

    class Meta:
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count',
        )
        model = User

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return Follow.objects.filter(user=user, following=obj.id).exists()

    def get_recipes(self, obj):
        page_size = 3
        recipes = Recipe.objects.filter(author=obj.following)
        paginator = Paginator(recipes, page_size)
        recipes_paginated = paginator.page(1)
        serializer = RecipeForFollowerSerializer(recipes_paginated, many=True)
        return serializer.data

    def get_recipes_count(self, obj):
        return Recipe.objects.filter(
            author=obj.following
        ).exclude(name__exact='').count()
