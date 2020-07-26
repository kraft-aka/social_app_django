from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Tag
from .forms import TagForm


@login_required
def tag_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    posts = tag.posts.all()
    return render(request, 'tags/tag_detail.html', locals())


@login_required
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', locals())


@login_required
def tag_update(request, pk):
    tag = Tag.objects.get(pk = pk)
    if request.method == 'POST':
        form = TagForm(
            request.POST or None,
            instance=tag)
        if form.is_valid():
            form.save()
        return redirect(tag.get_absolute_url())
    else:
        form = TagForm(initial={'title': tag.title})
    return render(request, 'tags/tag_update.html', locals())


@login_required
def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(form.instance.get_absolute_url())
    else:
        form = TagForm()
    return render(request, 'tags/tag_create.html', locals())
