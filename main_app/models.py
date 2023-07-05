from django.db import models

# Create your models here.
class Coral(models.Model):
    name = models. CharField(max_length= 100)
    img = models. CharField(max_length=250)
    info = models. TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        ordering =["name"]

class CoralTraits(models.Model):
    diet = models.CharField(max_length=100)
    toxicity_level =models.CharField(max_length=50)
    rareity = models.CharField(max_length= 50)
    coral = models.ForeignKey(Coral, on_delete=models.CASCADE, related_name='traits')
    
    def __str__(self):
        return self.diet

    class Meta:
        ordering =["diet"]

