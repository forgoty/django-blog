from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags', 'date_pub']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags', 'date_pub']


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
