from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/create/', views.TodoCreate.as_view(), name='todo-create'),              #to create new todo
    path('<int:user_id>/', views.TodoList.as_view(), name='todo-lists'),                        #to get all todos created by user
    path('<int:user_id>/<int:pk>/', views.TodoDetail.as_view(), name='todo-details'),           #to get todo details
    path('<int:user_id>/<int:pk>/update/', views.TodoUpdate.as_view(), name='todo-update'),     #to update todo
    path('<int:user_id>/<int:pk>/delete/', views.TodoDelete.as_view(), name='todo-delete'),                #to delete todo

    path('<int:user_id>/completed/', views.TodoCompletedList.as_view(), name='completed-todo'),           #to get all completed todo by user
    path('<int:user_id>/uncompleted/', views.TodoUncompletedList.as_view(), name='uncompleted-todo'),     #to get all uncompleted todo  by user
]