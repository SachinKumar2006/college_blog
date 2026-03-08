from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request):

    query = request.GET.get('q')
    post_list = Post.published.all()
    
    if query:
        
        post_list = post_list.filter(title__icontains=query)
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    latest_posts = Post.published.order_by('-publish')[:5]

    context = {
        'posts': posts,
        'latest_posts': latest_posts,
        'query': query
    }

    return render(request, 'blog/post/list.html', context)

def post_detail(request, year, month, day, slug):

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    latest_posts = Post.published.order_by('-publish')[:5]

    context = {
        'post': post,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/post/detail.html', context)