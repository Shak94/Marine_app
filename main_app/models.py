from django.db import models

# Create your models here.
class Coral(models.Model):
    name = models. CharField(max_length= 100)
    img = models. CharField(max_length=250)
    info = models. TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        ordering =["name"]