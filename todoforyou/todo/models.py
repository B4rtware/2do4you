from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Todo(models.Model):
    description = models.CharField(max_length=255) # not really restricted 
    deadline = models.DateField()
    progress = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    created = models.DateTimeField(auto_now_add=True)
