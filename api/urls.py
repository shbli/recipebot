from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'recipes', views.RecipeViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'cuisines', views.CuisineViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]