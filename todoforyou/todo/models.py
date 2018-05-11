from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

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
<<<<<<< HEAD
    importance = models.IntegerField(choices=IMPORTANCE_CHOICES, default=IMPORTANCE_CHOICES[1][0])

    class Meta:
        ordering = ["-importance"]

class TodoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
=======
    importance = models.IntegerField(choices=IMPORTANCE_CHOICES, default=IMPORTANCE_CHOICES[0][0])
>>>>>>> 9b42d75add291aaef455058562181d3298ea745b
