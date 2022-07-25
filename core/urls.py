from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('addtocart/<str:pk>/', views.addtocart, name='addtocart'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
