from .models import *
from rest_framework import serializers

class  PostSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post