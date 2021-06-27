from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_lists, name='todo-lists'),
    path('completed/', views.get_completed_todo_list, name='completed-todo'),
    path('uncompleted/', views.get_uncompleted_todo_list, name='uncompleted-todo'),
    path('create/', views.todo_create, name='todo-create'),
    path('details/<int:pk>/', views.todo_detail, name='todo-details'),
    path('update/<int:pk>/', views.todo_update, name='todo-update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo-delete'),
]