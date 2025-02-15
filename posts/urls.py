from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    LikePostView,
    CommentPostView,
    PostStatsView,
)

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post_list_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="like_post"),
    path("posts/<int:pk>/comment/", CommentPostView.as_view(), name="comment_post"),
    path("posts/<int:pk>/stats/", PostStatsView.as_view(), name="post_stats"),
]
