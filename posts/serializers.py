from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
# field I want to share
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post
