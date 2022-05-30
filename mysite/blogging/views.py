from email.policy import HTTP
from http.client import HTTPResponse
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from blogging.models import Post

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    # model = Post
    # queryset = Post.objects.all()
    queryset = Post.objects.exclude(published_date__exact=None).order_by("-published_date")
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
