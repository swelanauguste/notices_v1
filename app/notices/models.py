import os

from django.db import models
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("category",)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category.capitalize()


class Notice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categories",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50, default="admin")
    
    class Meta:
        ordering = ('-updated_at',)

    def get_absolute_url(self):
        return reverse("notice-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class NoticeFile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doc_name = models.CharField(max_length=100, blank=True, null=True)
    notice = models.ForeignKey(
        Notice, on_delete=models.CASCADE, null=True, blank=True, related_name="files"
    )
    doc = models.FileField(upload_to="notice_files")

    def get_file_name(instance, filename):
        return f"{filename}"

    def save(self, *args, **kwargs):
        self.doc_name = self.get_file_name(self.doc).replace('notice_files/', 'new')
        super(NoticeFile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.notice.title} - {self.doc_name}"
