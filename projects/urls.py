from django.urls import path, include
from . import views

app_name = 'projects'

urlpatterns = [
    path('project/', views.project_list, name='list'),
    path('project/new', views.project_new, name='new'),
    path('project/<int:pk>/edit', views.project_edit, name='edit'),
    path('project/<int:pk>/detail', views.project_detail,name='detail'),
    # path('project/add', views.signin, name='project_new'),
    # path('project/<int:pk>', views.singout, name='project_detail'),
    path('', views.index, name='index'),
]