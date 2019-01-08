''' Here is module with private functions, designed for developer
purposes'''

from django.db.models import Q

from blog.models import Post


def get_posts(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) |
                                    Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    return posts


def get_next_url(page):

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    return next_url


def get_prev_url(page):

    if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    return prev_url
