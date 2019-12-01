from django.contrib.auth.models import User
from django.db import models


class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    following = models.ManyToManyField('self', related_name='following')

    def __str__(self):
        return self.user.username
