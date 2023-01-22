from django.contrib import admin

from .models import Author, Category, Notice, NoticeFile, NoticeStatus

admin.site.register(Notice)
admin.site.register(NoticeFile)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(NoticeStatus)
