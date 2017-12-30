from rest_framework import viewsets

from . import models
from . import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides access to recipes

    list:
    Retrieves a list of recipes stored in the database

    retrieve:
    Retrieves a single recipe

    create:
    Stores a new recipe

    destroy:
    Removes an existing recipe

    update:
    Updates an existing recipe

    partial_update:
    Updates specific fields on an existing recipe
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides access to categories.

    retrieve:
    Retrieves a category

    list:
    Retrieves all possible categories

    create:
    Stores a new category

    destroy:
    Removes a category

    update:
    Updates an existing category

    partial_update:
    Updates specific fields of an existing category

    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'


class CuisineViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides access to cuisines

    list:
    Retrieves a list of cuisines stored in the database

    retrieve:
    Retrieves a single cuisine

    create:
    Stores a new cuisine

    destroy:
    Removes an existing cuisine

    update:
    Updates an existing cuisine

    partial_update:
    Updates specific fields on an existing cuisine
    """
    queryset = models.Cuisine.objects.all()
    serializer_class = serializers.CuisineSerializer
    lookup_field = 'slug'


class CourseViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides access to course

    list:
    Retrieves a list of courses stored in the database

    retrieve:
    Retrieves a single course

    create:
    Stores a new course

    destroy:
    Removes an existing course

    update:
    Updates an existing course

    partial_update:
    Updates specific fields on an existing course
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    lookup_field = 'slug'
