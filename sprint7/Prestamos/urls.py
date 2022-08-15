from django.urls import path
from . import views

urlpatterns = [
    path('loan-validation/<str:username>/',
         views.validation, name='validation'),
]
