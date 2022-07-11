from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
	path('register/', views.register_user, name="register_user"),
	path('login_users/', views.login_users, name="login_users"),
	path('logout_users/', views.logout_users, name='logout'),
]