from django.db import models
from django.urls import reverse

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

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gos', kwargs={'gos_slug': self.slug})

class Room(models.Model):
    class Status(models.IntegerChoices):
        OCCUPIED = 0, 'Занят'
        AVAILABLE = 1, 'Свободен'

    hotel = models.ForeignKey(Gostinitsa, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=100)
    is_status = models.IntegerField(choices=Status.choices, default=Status.AVAILABLE)

    objects = models.Manager()
    status = StatusManager()

    def __str__(self):
        return self.room_number


