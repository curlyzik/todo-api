from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import Todo

from .mixins import MultipleFieldLookupMixin
from .serializers import TodoModelSerializer


# CREATE A NEW TODO
class TodoCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoModelSerializer
    lookup_field = ['user_id']

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

# GET ALL TODOS CREATED BY USER
class TodoList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    lookup_field = ['user_id']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user.id)

# GET TODO DETAIL
class TodoDetail(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    lookup_fields = ['user_id','pk']

# TO UPDATE TODO
class TodoUpdate(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    lookup_fields = ['user_id','pk']

# TO DELETE TODO
class TodoDelete(MultipleFieldLookupMixin, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    lookup_fields = ['user_id','pk']

# GET ALL COMPLETED TODOS BY USER
class TodoCompletedList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    lookup_field = ['user_id']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user.id, completed=True)

# GET ALL UNCOMPLETED TODOS BY USER
class TodoUncompletedList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    lookup_field = ['user_id']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user.id, completed=False)