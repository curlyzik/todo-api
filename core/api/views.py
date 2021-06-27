from core.models import Todo
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TodoModelSerializer


# CREATING NEW TODO APP
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def todo_create(request):
    data = request.data
    user = request.user
    try:
        new_todo = Todo.objects.create(
            user = user,
            title = data['title'],
            description = data['description'],
            completed = data['completed'],
        )

        serializer = TodoModelSerializer(new_todo, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response({'detail':"Can't create post"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todo_lists(request):
    user = request.user
    todos = Todo.objects.filter(user=user)

    serializer = TodoModelSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todo_detail(request, pk):
    user = request.user
    try:
        todo = Todo.objects.get(pk=pk)
        if todo.user == user:
            serializer = TodoModelSerializer(todo, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {'detail': 'You cant view this todo'}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)
    except Todo.DoesNotExist:
        return Response({'detail': "Todo doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def todo_update(request, pk):
    user = request.user
    data = request.data
    todo = Todo.objects.get(pk=pk)

    if todo.user == user:
        todo.title = data['title']
        todo.description = data['description']
        todo.completed = data['completed']

        todo.save()
        serializer = TodoModelSerializer(todo, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        message = {'detail': 'You are not authorized to update this todo'}
        return Response(message, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def todo_delete(request, pk):
    user = request.user
    todo = Todo.objects.get(pk=pk)

    if todo.user == user:
        todo.delete()
        message = {'detail': 'Todo deleted successfully'}
        return Response(message, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'You are not authorized to delete this todo'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_completed_todo_list(request):
    user = request.user
    completed_todo = Todo.objects.filter(user=user, completed=True)

    serializer = TodoModelSerializer(completed_todo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_uncompleted_todo_list(request):
    user = request.user
    uncompleted_todo = Todo.objects.filter(user=user, completed=False)

    serializer = TodoModelSerializer(uncompleted_todo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
