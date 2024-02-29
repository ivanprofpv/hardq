
from django.conf.urls.static import static
from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('re/', group_students, name='rebuild'),
]