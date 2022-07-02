from .views import GetUser, CreateUser, UserByID
from django.urls import path
import djoser.urls
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/users/', GetUser.as_view()),
    path('api/users/<int:pk>', UserByID.as_view()),
    path('api/users/create/', CreateUser.as_view())

]
