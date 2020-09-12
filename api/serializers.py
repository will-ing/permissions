from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user', 'title', 'director', 'cast', 'release')
        model = Post
