from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify


class Category(models.Model):
    user = models.ForeignKey(User, related_name="category_created", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']


class Card(models.Model):
    user = models.ForeignKey(User, related_name="cards_created", on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, verbose_name="category",
                                 related_name="category_created", on_delete=models.CASCADE)
    title_native_language = models.CharField(max_length=255)
    translate_studied_language = models.CharField(max_length=255)
    usage_example = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title_native_language

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_native_language)
        return super(Card, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_slug': self.slug})

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        ordering = ['time_create', 'title_native_language']
