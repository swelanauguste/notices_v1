import django_filters
from django import forms

from .models import Category, Notice


class NoticeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Title",
        widget=forms.TextInput(attrs={"class": "rounded-pill"}),
    )

    # category = django_filters.ModelChoiceFilter(
    #     queryset=Category.objects.all(),
    #     widget=forms.Select(attrs={"class": "rounded-pill"}),
    # )

    class Meta:
        model = Notice
        fields = ("title",)
