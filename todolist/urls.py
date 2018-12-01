from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('details/<pk>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('delete/<pk>', views.delete, name='delete'),
    path('profile/', views.profile, name='profile'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('edit_todo/<pk>', views.edit_todo, name='edit_todo'),
    path('404/', views.errorpage, name='errorpage'),
]
