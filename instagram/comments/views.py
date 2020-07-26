from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .models import Comment
from .forms import CommentForm


def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == "POST":
        if comment.user == request.user:
            comment.delete()
            return redirect(post.get_absolute_url())
        else:
            return HttpResponseForbidden()
    return HttpResponse({"detail": "ok"}) 


def update_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == "POST":
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm(initial={'content': comment.content})
    return render(request, 'posts/update_comment.html', locals())

