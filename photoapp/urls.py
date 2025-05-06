
# photoapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_talking_photo, name='create_talking_photo'),
    path('result', views.show_result, name='show_result'),
]
