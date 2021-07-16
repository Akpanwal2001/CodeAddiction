from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=30, default="Code Addiction")
    slug = models.CharField(max_length=120)
    thumbnail = models.ImageField(upload_to = 'images/', default = "")
    content = FroalaField()
    view = models.IntegerField(default=0)
    short_content = models.TextField(max_length=400, default="")
    datetime = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
