from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet


class Notifications(models.Model):
    '''
    tweet - FK \n
    twitter_user - FK \n
    tweet_viewed - Boolean
    '''
    tweet = models.ForeignKey(
        Tweet, related_name="notification_tweet", on_delete=models.CASCADE)
    twitter_user = models.ForeignKey(
        TwitterUser,
        related_name='notification_user',
        on_delete=models.CASCADE)
    tweet_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.twitter_user}-{self.tweet}"
