from django.urls import path

from .views import NoticeListView, NoticeDetailView, NoticeCreateView


urlpatterns = [
    path('', NoticeListView.as_view(), name='notice-list'),
    path('detail/<int:pk>/', NoticeDetailView.as_view(), name='notice-detail'),
    path('create/', NoticeCreateView.as_view(), name='notice-create'),

]