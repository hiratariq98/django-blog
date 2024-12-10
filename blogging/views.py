from django.http.response import HttpResponse, Http404
from django.shortcuts import render
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import loader

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Keyword args: \n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=False).order_by('-published_date')


class BlogDetailView(DetailView):
    model = Post
    Post.objects.filter(published_date__isnull=False)
    template_name = 'blogging/detail.html'
