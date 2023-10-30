from django.db import models

from users.models import Pal


class PantryItem(models.Model):
    pal = models.ForeignKey(
        to=Pal,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=20,
    )
    quantity = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f'{self.pal}\'s {self.name}'