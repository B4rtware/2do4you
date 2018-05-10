from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Todo(models.Model):
    IMPORTANCE_CHOICES = (
        (000, 'white'),
        (100, 'green'),
        (200, 'orange'),
        (300, 'red'),
    )
    description = models.CharField(max_length=255) # not really restricted 
    deadline = models.DateField()
    progress = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    created = models.DateTimeField(auto_now_add=True)
    importance = models.IntegerField(choices=IMPORTANCE_CHOICES, default=IMPORTANCE_CHOICES[1][0])