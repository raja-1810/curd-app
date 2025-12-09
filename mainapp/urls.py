from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, dashboard, get_books_from_api

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard),
    path('api/books/', get_books_from_api, name='get_books'), 
]
