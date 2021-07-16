from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=12)
    content = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "message from : " + self.name + " by " + self.email