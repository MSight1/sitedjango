from django.db import models
from django.urls import reverse


class Gostinitsa(models.Model):
    title = models.CharField(max_length=255) #название
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True) #текст про гостиницу ( ну типа вид создать )
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gos', kwargs={'gos_slug':self.slug})