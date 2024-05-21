from django.urls import path
from swanapp import views

urlpatterns=[
    path('home/', views.firstView),
]
