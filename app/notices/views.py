from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .models import Notice


class NoticeListView(ListView):
    model = Notice


class NoticeDetailView(DetailView):
    model = Notice


class NoticeCreateView(CreateView):
    model = Notice
    fields = ["category", "title", "content", "author"]
