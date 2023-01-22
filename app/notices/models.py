import os

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.category:
            # Newly created object, so set slug
            self.category = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ("category",)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category.capitalize()


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True, default="758")
    tel1 = models.CharField(max_length=15, blank=True, null=True, default="758")
    tel2 = models.CharField(max_length=15, blank=True, null=True, default="758")
    fax = models.CharField(max_length=15, blank=True, null=True, default="758")
    email = models.EmailField(max_length=254, blank=True, null=True, default=".govt.lc")

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name.title()} {self.last_name.title()}"
        return f"{self.post.title()} {self.department.title()}"


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
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notice_author_list",
    )

    class Meta:
        ordering = ("-updated_at",)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(Notice, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("notice-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title.title()


class NoticeFile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doc_name = models.CharField(max_length=255, blank=True, null=True)
    notice = models.ForeignKey(
        Notice, on_delete=models.CASCADE, null=True, blank=True, related_name="files"
    )
    doc = models.FileField(upload_to="notice_files")

    def get_file_name(instance, filename):
        return f"{filename}"

    def save(self, *args, **kwargs):
        self.doc_name = self.get_file_name(self.doc).replace("notice_files/", "new")
        super(NoticeFile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.notice.title} - {self.doc_name}"
