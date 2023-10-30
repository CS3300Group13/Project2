from django.db import models
from django.contrib.auth.models import User



class Pal(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    about = models.TextField(
        max_length=500,
        null=True,
        blank=True,
    )
    following = models.ManyToManyField(
        to='self', 
        related_name='followers', 
        symmetrical=False,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f'{self.user.first_name}'

