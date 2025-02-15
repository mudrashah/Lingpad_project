from rest_framework import serializers
from .models import Post, Comment
from users.models import User
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    def get_comment(self, obj):
        comments = Comment.objects.filter(post=obj)
        return CommentSerializer(comments, many=True).data

    def get_author(self, obj):
        author = User.objects.filter(id=obj.author_id)
        return UserSerializer(author, many=True).data

    class Meta:
        model = Post
        fields = "__all__"


class UpdatePostSerializer(serializers.ModelSerializer):

    def update(self, instance, data):
        instance.title = data["title"]
        instance.content = data["content"]
        instance.category = data["category"]
        instance.save()
        return instance

    def create(self, data):
        data["author"] = self.context["request"].user
        return Post.objects.create(**data)

    class Meta:
        model = Post
        fields = ("title", "content", "category")
