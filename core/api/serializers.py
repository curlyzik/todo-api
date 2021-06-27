from rest_framework import serializers
from core.models import Todo

class TodoModelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Todo
        fields = ['user','id', 'title', 'description', 'completed', 'created']
    
    def get_user(self,obj):
        user = obj.user.email
        return user