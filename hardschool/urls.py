from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'teachers', views.TeacherViewSet)

urlpatterns = [
    path('re/', group_students, name='rebuild'),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
