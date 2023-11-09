from django.db import models

class Gostinitsa(models.Model):
    title = models.CharField(max_length=255) #название
    content = models.TextField(blank=True) #текст про гостиницу ( ну типа вид создать )
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)