from django.urls import path
from rest_framework.authtoken import views

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
    
    path('tags/', TagListAPIView.as_view(), name='api.tags_list'),
    path('tag/create/', TagCreateAPIView.as_view(), name='api.tag_create'),
    path('tag/<str:slug>/update/', TagUpdateAPIView.as_view(), name='api.tag_update'),
    path('tag/<str:slug>/delete/', TagDeleteAPIView.as_view(), name='api.tag_delete'),
    path('auth/', views.obtain_auth_token),
]
