from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, related_name="notification_tweet", on_delete=models.CASCADE)
    twitter_user = models.ForeignKey(TwitterUser, related_name='notification_user', on_delete=models.CASCADE)
    tweet_viewed = models.BooleanField(default=False)
