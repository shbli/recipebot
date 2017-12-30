from rest_framework import viewsets

from . import models
from . import serializers


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint provides access to recipes

    list:
    Retrieves a list of recipes stored in the database

    retrieve:
    Retrieves a single recipe
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    lookup_field = 'slug'

    def get_serializer(self, *args, **kwargs):
        if self.action == 'list':
            kwargs['context'] = self.get_serializer_context()
            return serializers.RecipeSummarySerializer(*args, **kwargs)

        return super().get_serializer(*args, **kwargs)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint provides access to categories.

    retrieve:
    Retrieves a category

    list:
    Retrieves all possible categories
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'


class CuisineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint provides access to cuisines

    list:
    Retrieves a list of cuisines stored in the database

    retrieve:
    Retrieves a single cuisine
    """
    queryset = models.Cuisine.objects.all()
    serializer_class = serializers.CuisineSerializer
    lookup_field = 'slug'


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint provides access to course

    list:
    Retrieves a list of courses stored in the database

    retrieve:
    Retrieves a single course
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    lookup_field = 'slug'
