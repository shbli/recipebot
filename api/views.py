from rest_framework import viewsets

from . import models
from . import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'


class CuisineViewSet(viewsets.ModelViewSet):
    queryset = models.Cuisine.objects.all()
    serializer_class = serializers.CuisineSerializer
    lookup_field = 'slug'


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    lookup_field = 'slug'
