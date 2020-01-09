from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.models import Tweet
from twitterclone.tweets.forms import AddTweetForm
import re
from twitterclone.notifications.models import Notifications
from twitterclone.twitterusers.models import TwitterUser
from django.views import View
from django.utils.decorators import method_decorator


class ViewTweet(View):
    def get(self, request, id):
        html = 'tweet/view_tweet.html'
        data = Tweet.objects.filter(id=id)
        return render(request, html, {'data': data})


@method_decorator(login_required, name='dispatch')
class ViewHomePage(View):
    def get(self, request):
        html = 'index.html'
        following = request.user.twitteruser.following.all()
        data = Tweet.objects.filter(
            tweet_author__in=following).order_by('-post_date')
        return render(request, html, {'data': data})


@login_required
def make_tweets(request):
    html = 'add_tweet.html'
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                tweet_author=request.user.twitteruser,
                body=data['body']
            )
            if '@' in data['body']:
                usernames = re.findall(r'@(\w+)', data['body'])
                for username in usernames:
                    twitteruser = TwitterUser.objects.get(
                        user__username=username)
                    Notifications.objects.create(
                        tweet=tweet,
                        twitter_user=twitteruser
                    )
        return HttpResponseRedirect(reverse('homepage'))
    form = AddTweetForm()
    return render(request, html, {'form': form})
