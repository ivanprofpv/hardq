from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'api/products', views.ProductViewSet)
router.register(r'api/lessons', views.LessonViewSet, basename='lesson')
router.register(r'teachers', views.TeacherViewSet)

urlpatterns = [
    path('re/', group_students, name='rebuild'),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/average_number_in_percentage/', AverageNumberInPercentageAPIView.as_view(), name='group-fill-percentage'),
]

urlpatterns += router.urls
