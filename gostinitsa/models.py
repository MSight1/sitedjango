from django.contrib.auth import forms
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


def traislit_to_end(s: str) -> str:  #костыль для перевода русского текста в слаг транслитом
    d = {'а': 'a', 'б':'b', 'в':'v','г':'g', 'д':'d', 'е':'e', 'ё':'yo', 'ж':'zh', 'з':'z',
    'и':'i', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t',
    'у':'y', 'ф':'f', 'х':'h', 'ц':'c', 'ч':'ch', 'ш':'sh', 'щ':'shch', 'ь':'', 'ы':'y', 'ъ':'', 'э':'r', 'ю':'yu', 'я':'ya'}
    return "".join(map(lambda x:d[x] if d.get(x,False) else x, s.lower()))
class PublishedManager(models.Manager): #
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Gostinitsa.Status.PUBLISHED)

class  StatusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_status=Room.Status.AVAILABLE)

class Gostinitsa(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]),x[1]),Status.choices)), default=Status.DRAFT, verbose_name='Опубликовано')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Гостиницы'
        verbose_name_plural = 'Гостиницы'
        ordering = ['-time_create']
        indexes = [models.Index(fields=['-time_create'])]
    def get_absolute_url(self):
        return reverse('gos', kwargs={'gos_slug': self.slug})
    # save(self, *args, **kwargs):
      #  self.slug=slugify(traislit_to_end(self.title))
       # super().save(*args, **kwargs)

class Room(models.Model):
    class Status(models.IntegerChoices):
        AVAILABLE = 1, 'Свободен'
        OCCUPIED = 0, 'Занят'

    hotel = models.ForeignKey(Gostinitsa, on_delete=models.CASCADE, verbose_name='Принадлежит гостинице')
    room_number = models.CharField(max_length=100, verbose_name='Номер комнаты')
    is_status = models.IntegerField(choices=Status.choices, default=Status.AVAILABLE, verbose_name='Статус')

    objects = models.Manager()
    status = StatusManager()

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
        ordering = ['hotel' , 'room_number']
        indexes = [models.Index(fields=['room_number'])]
    def __str__(self):
        return self.room_number


###Пользователь
