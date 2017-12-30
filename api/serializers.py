from rest_framework import serializers
from . import models


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='recipe-detail',
        lookup_field='slug'
    )

    class Meta:
        model = models.Recipe
        exclude = ('version',)
        read_only_fields = ['created', 'modified', 'slug']
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
