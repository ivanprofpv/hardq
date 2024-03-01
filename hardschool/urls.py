from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'lessons', views.LessonViewSet, basename='lesson')
router.register(r'teachers', views.TeacherViewSet)

urlpatterns = [
    path('re/', group_students, name='rebuild'),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('lessons/<int:user_id>/', views.LessonViewSet.as_view({'get': 'list'}), name='lesson-list'),
]

urlpatterns += router.urls
