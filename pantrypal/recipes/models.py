from django.db import models

from users.models import Pal


class Recipe(models.Model):
    pal = models.ForeignKey(
        to=Pal,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
    )
    steps = models.TextField(
        max_length=1000,
    )
    
    def __str__(self):
        return f'{self.name}'
