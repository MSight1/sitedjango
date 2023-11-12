from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):  #класс для отображения только тех гостиниц, которые опубликованы
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Gostinitsa.Status.PUBLISHED)
class Gostinitsa(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255) #название
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True) #текст про гостиницу ( ну типа вид создать )
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices,default=Status.DRAFT)

    object = models.Manager() #чтобы Gostinitsa.objects продолжали работать
    published = PublishedManager() #для работы класса отображения гостиниц
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gos', kwargs={'gos_slug':self.slug})