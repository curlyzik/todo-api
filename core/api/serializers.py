from rest_framework import serializers
from core.models import Todo

class TodoModelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Todo
        fields = ['user', 'user_id', 'id', 'title', 'description', 'completed', 'created']
    
    def get_user(self,obj):
        user = obj.user.email
        return user
    
    def get_user_id(self,obj):
        user_id = obj.user.id
        return user_id