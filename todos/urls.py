from django.urls import path
from todos import views

app_name = 'todos'

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='user_logout'),
	path('login/', views.user_login, name='user_login')
]
