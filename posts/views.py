from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Posts
from .forms import PostForm

# Create your views here.


def post_list(request):
    queryset = Posts.objects.all()
    context = {
        'title': 'list',
        'qs': queryset
    }

    return render(request, 'index.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect('/posts')
    else:
        messages.error(request, "Not Created!!")
    context = {
        'form': form,
    }
    return render(request, 'post_create.html', context)


def post_detail(request, pk=None):
    instance = get_object_or_404(Posts, id=pk)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'post_detail.html', context)


def post_update(request, pk=None):
    instance = get_object_or_404(Posts, id=pk)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/posts')
    else:
        messages.error(request, "Not Updated!!")
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'post_create.html', context)


def post_delete(request, pk=None):
    instance = get_object_or_404(Posts, id=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("postlist")
