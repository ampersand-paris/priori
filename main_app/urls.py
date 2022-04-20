from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="todos"),
    path('login/', views.login_view, name="login"),
    path('accounts/signup/', views.signup_view, name="signup"),
    path('todos/', views.Todos.as_view(), name="todos")
]