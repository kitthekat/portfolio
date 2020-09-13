from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from blog.models import Post, Comment
from blog.forms import CommentForm


def blog_index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog_index.html', {'posts': posts})


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request: HttpRequest, pk: str) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog_details.html', context)
