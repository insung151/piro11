from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(blank=True, null=True)
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
