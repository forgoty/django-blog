import os

from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

from .modules.privates import *
from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


def posts_list(request):
    POSTS_ON_PAGE = 5

    posts = get_posts(request)

    paginator = Paginator(posts, POSTS_ON_PAGE)

    #request.GET.get('page', 1 - default value if 'page' is not found)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    next_url = get_next_url(page)
    prev_url = get_prev_url(page)

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog/index.html', context=context)


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def about_blog_link(request):
    path = os.path.join(settings.BASE_DIR, 'static/about.md') 
    with open(path, 'r') as file:
        about = file.read()

    context = {
        'about': about
    }
    return render(request, 'blog/about.html', context=context)


def my_handler404(request, exception):
    data = {'123': '123'}
    return render(request, "blog/404.html", data)