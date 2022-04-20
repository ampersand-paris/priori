from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Todos.as_view(), name="todos"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup")
]