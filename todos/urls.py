from django.urls import path
from todos import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

app_name = 'todos'

urlpatterns = [
	path('', login_required(views.TaskList.as_view()), name='index'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='user_logout'),
	path('login/', views.user_login, name='user_login'),
	path('post/', views.todos_poster, name='post_todo'),
	url(r'^(?P<pk>[0-9]+)/$', login_required(views.TaskDetail.as_view()), name='detail_todo'),
	url(r'^(?P<pk>[0-9]+)/update/$', login_required(views.TaskUpdate.as_view()), name='update_todo'),
	url(r'^(?P<pk>[0-9]+)/delete/$', login_required(views.TaskDelete.as_view()), name='delete_todo'),
]
