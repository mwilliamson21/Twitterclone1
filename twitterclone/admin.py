from django.contrib import admin
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from twitterclone.notifications.models import Notifications

admin.site.register(TwitterUser)
admin.site.register(Tweet)
admin.site.register(Notifications)
