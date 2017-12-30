from rest_framework import serializers
from . import models


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measurement
        fields = ('name',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ('name',)


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    unit = MeasurementSerializer(read_only=True)

    class Meta:
        model = models.RecipeIngredient
        fields = ('ingredient', 'amount', 'unit')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='recipe-detail',
        lookup_field='slug'
    )

    ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = models.Recipe
        fields = (
        'name', 'description', 'cooking_instructions', 'preparation_time', 'cooking_time', 'category', 'course',
        'cuisine', 'ingredients', 'created','modified','url')
        read_only_fields = ['created', 'modified']
        extra_kwargs = {
            'course': {
                'lookup_field': 'slug'
            },
            'cuisine': {
                'lookup_field': 'slug'
            },
            'category': {
                'lookup_field': 'slug'
            }
        }
        lookup_field = 'slug'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name',)
        lookup_field = 'slug'


class CuisineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cuisine
        fields = ('id', 'name', 'slug')
        lookup_field = 'slug'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'slug')
        lookup_field = 'slug'
