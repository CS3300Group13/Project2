from django.db import models

from users.models import Pal


class Post(models.Model):
    pal = models.ForeignKey(
        to=Pal,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        max_length=500,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f'{self.pal}\'s {self.pk} post'
    
    
class Like(models.Model):
    pal = models.ForeignKey(
        to=Pal,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f'{self.pal} liked {self.post.pal}\'s post'
