from django.contrib import admin
from .models import Category, Notice, NoticeFile

admin.site.register(Notice)
admin.site.register(NoticeFile)
admin.site.register(Category)
