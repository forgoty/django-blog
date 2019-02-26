from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags', 'date_pub']
