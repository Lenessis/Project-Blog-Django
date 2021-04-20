from django.http import Http404
from django.shortcuts import render

from .models import Post


def post_list(request):
    latest_post_list = Post.objects.order_by('-publish')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'mainapp/home.html', context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        comments = Comment.objects.get(fk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'mainapp/post_detail.html', {'post': post,'comments': comments})