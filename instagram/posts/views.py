from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.db.models import Q

from comments.models import Comment
from .models import Post
from .forms import PostForm

User = get_user_model()


def main_page(request):
    search_user = request.GET.get('search', '')
    if search_user:
        users = User.objects.filter(
        Q(username__icontains=search_user))
    else:
        users = User.objects.all().exclude(username=request.user.username)
    return render(request, 'base.html', locals())


@login_required
def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | 
            Q(description__contains=search_query)
        )
    else:
        posts = Post.objects.all()

    # user = request.user
    # user_followings = user.profile.followings.all()
    # posts = []
    # for u in user_followings:
    #     for post in u.user.posts.all():
    #         posts.append(post)
    return render(request, 'posts/posts_list.html', locals())


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.post_comments.all()[:10]
    user_obj = request.user
    if request.method == "POST":
        if user_obj in post.likes.all():
            post.likes.remove(user_obj)
        else:
            post.likes.add(user_obj)
        return redirect(post.get_absolute_url())
    return render(request, 'posts/post_detail.html', locals())


@login_required
def bookmark_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user_obj = request.user
    if request.method == "GET":
        if post in  user_obj.profile.bookmarks.all():
            user_obj.profile.bookmarks.remove(post)
        else:
            user_obj.profile.bookmarks.add(post)
        return redirect(post.get_absolute_url())


@login_required
def post_likes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    likes = post.likes.all()
    return render(request, 'posts/post_likes.html', locals())


@login_required
def post_create(request):
    if request.method == "POST":
        # title = request.POST.get('title')
        # descr = request.POST.get('descr')
        # image = request.FILES.get('image')
        # post = Post.objects.create(title=title, description=descr, image=image)
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
        return redirect(form.instance.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', locals())


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('posts-list')
    return render(request, 'posts/confirm_delete.html')


@login_required
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        # post.title = request.POST.get('title')
        # post.description = request.POST.get('descr')
        # post.image = request.FILES.get('image')
        # post.save()
        form = PostForm(
            request.POST or None,
            request.FILES or None, 
            instance=post)
        if form.is_valid():
            form.save()
        return redirect(post.get_absolute_url())
    else:
        form = PostForm(initial={'title': post.title, 'description': post.description})
    return render(request, 'posts/post_update.html', locals())



@login_required
def comment_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    if request.method == "POST":
        text = request.POST.get('q')
        comment = Comment.objects.create(
            post=post, user=user, content=text)
        return redirect(post.get_absolute_url())
    return HttpResponse({"detail": "ok"})


@login_required
def like_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    user = request.user
    if request.method == "POST":
        if user not in comment.likes.all():
            comment.likes.add(user)
        else:
            comment.likes.remove(user)
        return redirect(comment.post.get_absolute_url())
    return HttpResponse({'detail': 'ok'})

