from django.db import models
from django.utils import timezone
from twitterclone.twitterusers.models import TwitterUser


class Tweet(models.Model):
    TweetAuthor = models.ForeignKey(TwitterUser, related_name='tweet_author', on_delete=models.CASCADE)
    body = models.TextField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(TwitterUser, related_name='likes')
    dislikes = models.ManyToManyField(TwitterUser, related_name='dislikes')
    