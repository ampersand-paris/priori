from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="todos"),
    path('login/', views.login_view, name="login"),
    path('accounts/signup/', views.signup_view, name="signup"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('profile/days/', views.Days.as_view(), name="days"),
    path('profile/days/<int:pk>', views.Days_Update.as_view(), name="days_update"),
    path('profile/<int:pk>', views.Task_Update.as_view(), name="update"),
    path('profile/<int:pk>/delete/', views.Task_Delete.as_view(), name="delete"),

]