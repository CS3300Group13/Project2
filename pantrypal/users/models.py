from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import requests
from io import BytesIO

response = requests.get("https://bootdey.com/img/Content/avatar/avatar6.png")
img = Image.open(BytesIO(response.content))

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

