from django.db import models
import os

# Create your models here.

DEFAULT_STATUS = "draft"

STATUS = [
    ("draft", "Taslak"),
    ("published", "Yayınlandı"),
    ("deleted", "Silindi"),
]

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default="",)
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to="",
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Carousel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to="carousel",
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

