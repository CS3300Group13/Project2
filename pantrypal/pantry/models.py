from django.db import models

from users.models import Pal


class PantryItem(models.Model):

    foodGroups = [("Grains", "Grains"), ("Proteins", "Proteins"), ("Dairy", "Dairy"),
                  ("Fruits", "Fruits"), ("Vegetables", "Vegetables"),
                  ("Oils", "Oils"), ("Condiments", "Condiments")]


    pal = models.ForeignKey(
        to=Pal,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=20,
    )
    foodGroup = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices = foodGroups,
    )
    
    def __str__(self):
        return f'{self.pal}\'s {self.name}'