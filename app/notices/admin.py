from django.contrib import admin

from .models import Author, Category, Notice, NoticeFile, NoticeStatus

# admin.site.register(Notice)
# admin.site.register(NoticeFile)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(NoticeStatus)

class NoticeFileInline(admin.TabularInline):
    model = NoticeFile
    extra = 3
    
class NoticeAdmin(admin.ModelAdmin):
    inlines = (NoticeFileInline,)
    
admin.site.register(Notice, NoticeAdmin)