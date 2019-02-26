from django.urls import path

from .views import *


urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('<str:pk>/', PostDetailAPIView.as_view(), name='detail'),
    # path('post/create/', PostCreate.as_view(), name='post_create_url'),
    # path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    # path('post/<str:slug>/update/', PostUpdate.as_view(),
    #                                 name='post_update_url'),
    #
    # path('post/<str:slug>/delete/', PostDelete.as_view(),
    #                                 name='post_delete_url'),
    #
    # path('tags/', tags_list, name='tags_list_url'),
    # path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    # path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    # path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    # path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    # path('about/', about_blog_link, name='about_blog')
    #
]