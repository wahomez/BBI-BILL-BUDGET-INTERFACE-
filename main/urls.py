"""BBI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register_user, name="register"),
    path('budget/<str:pk>/', views.budget_page, name="budget"),
    path('budget-form/', views.budget_form, name="budget-form"),
    path('delete-budget/<str:pk>/', views.delete_budget, name="delete-budget"),
    path('budget-update/<str:pk>/', views.budget_update, name="budget-update"),
    path('profile/<str:pk>/', views.profile_page, name="profile"),
    path('profile-form/<str:pk>/', views.profile_form, name="profile-form"),
    path('bill/<str:pk>/', views.bill_page, name="bill"),
    path('bill-form/', views.bill_form, name="bill-form"),
    path('bill-update/<str:pk>/', views.bill_update, name="bill-update"),
    path('delete-bill/<str:pk>/', views.bill_delete, name="delete-bill"),
    path('logout/', views.logout_user, name="logout"),
    
]
