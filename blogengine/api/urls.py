from django.urls import path

from .views import *


urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='api.post_list'),
    path('post/create/', PostCreateAPIView.as_view(), name='api.post_create'),
    path('post/<str:slug>/', PostDetailAPIView.as_view(),
                                                    name='api.post_detail'),
    path('post/<str:slug>/update/', PostUpdateAPIView.as_view(),
                                                    name='api.post_update'),

    path('post/<str:slug>/delete/', PostDeleteAPIView.as_view(),
                                                    name='api.post_delete'),
    #
    # path('tags/', tags_list, name='tags_list_url'),
    # path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    # path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    # path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    # path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    # path('about/', about_blog_link, name='about_blog')
    #
]