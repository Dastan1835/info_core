from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Категории публикаций"
        verbose_name = "Категория публикации"

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Хештеги'
        verbose_name = 'Хештег'

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField(verbose_name="Изображения", null=True)
    shorts_description = models.CharField(verbose_name="кротький описание", max_length=255, null=True)
    description = RichTextField(null=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Публикация'
        verbose_name = 'Публикации'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()


class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user_name = models.CharField(max_length=255, null=True)


