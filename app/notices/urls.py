from django.urls import path

from .views import (
    NoticeCreateView,
    NoticeDetailView,
    NoticeDraftedListView,
    NoticePublishedListView,
)

urlpatterns = [
    path("", NoticePublishedListView.as_view(), name="notice-list"),
    path("drafted/", NoticeDraftedListView.as_view(), name="notice-drafted-list"),
    path("detail/<slug:slug>/", NoticeDetailView.as_view(), name="notice-detail"),
    path("create/", NoticeCreateView.as_view(), name="notice-create"),
]
