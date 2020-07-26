from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse

from .forms import LoginForm, OwnUserChangeForm
from .models import Profile



def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('posts-list')
    else:
        form = UserCreationForm()
    return render(request, 'users/sign_up.html', locals())


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_obj = get_object_or_404(User, username=username)

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('posts-list')
            return HttpResponse("Incorrect password or login")
    else:
        form = LoginForm()

    return render(request, 'users/sign_up.html', locals())


@login_required
def user_profile(request, pk):
    user_obj_profile = get_object_or_404(Profile, pk=pk)
    user_obj = user_obj_profile.user
    current_user_profile = request.user.profile
    if request.method == "POST":
        if request.user != user_obj:
            if user_obj_profile not in current_user_profile.followings.all():
                current_user_profile.follow(user_obj_profile)
            else:
                current_user_profile.unfollow(user_obj_profile)
            return redirect(user_obj_profile.get_absolute_url())
        return HttpResponse("You cannot follow yourself")
    return render(request, 'users/profile.html', locals())


@login_required
def my_bookmarks(request):
    user = request.user
    posts = user.profile.bookmarks.all()
    return render(request, 'posts/posts_list.html', locals())


@login_required
def user_posts(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = user.posts.all()
    return render(request, 'posts/posts_list.html', locals())


@login_required
def followers(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    follows = profile.followers.all()
    header = "Followers"
    return render(request, 'users/follows.html', locals())


@login_required
def followings(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    follows = profile.followings.all()
    header = "Followings"
    return render(request, 'users/follows.html', locals())


@login_required
def user_update(request):
    user_obj = request.user
    if request.method == 'POST':
        form = OwnUserChangeForm(
            request.POST or None,
            instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect(user_obj.profile.get_absolute_url())
    else:
        form = OwnUserChangeForm(initial={
            'username': user_obj.username,
            'first_name': user_obj.first_name,
            'last_name': user_obj.last_name,
            'email': user_obj.email,
            })
    return render(request, 'users/user_update.html', locals())


@login_required
def user_delete(request):
    user_obj = request.user
    if request.method == "POST":
        user_obj.delete()
        return redirect('sign-up')
    return render(request, 'users/confirm_delete.html',locals())