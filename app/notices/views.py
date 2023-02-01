from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .filter import NoticeFilter
from .models import Category, Notice


class NoticePublishedListView(ListView):
    model = Notice
    queryset = Notice.objects.filter(status__status__icontains="published")

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NoticeFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class NoticeDraftedListView(ListView):
    model = Notice
    queryset = Notice.objects.filter(status__status__icontains="draft")

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NoticeFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class NoticeDetailView(DetailView):
    model = Notice


class NoticeCreateView(CreateView):
    model = Notice
    fields = ["category", "title", "content", "author"]
