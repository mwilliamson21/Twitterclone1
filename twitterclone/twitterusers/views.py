from django.shortcuts import render, HttpResponseRedirect, reverse
# from twitterclone.twitteruser.forms import NewUserForm
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from twitterclone.notifications.models import Notifications
# from django.contrib.auth import login, logout


@login_required
def NewUserForm_view(request):
    html = 'NewUser.html'
    user = request.user
    twitteruser = TwitterUser.objects.get(user=user)
    notifications = Notifications.objects.filter(
        viewed=twitteruser, not_viewed=True)
    number_of_notifications = len(notifications)
    followed = twitteruser.following.all()
    tweets = Tweet.objects.filter(author__in=followed).ordered_by(
        '-post_date')

    number_following = len(followed)
    return render(request, html, {
        'twitteruser': twitteruser,
        'number_following': number_following,
        'followed': followed,
        'tweets': tweets,
        'number_of_notifications': number_of_notifications
    })


def profile_view(request, id):
    html = 'user_profile.html'
    twitteruser = TwitterUser.objects.filter(id=id).first()
    tweets = Tweet.objects.filter(
        tweet_author=twitteruser).order_by('-post_date')
    return render(request, html, {
        'tweets': tweets, 'twitteruser': twitteruser})


def follow_user(request, id):
    follow_user = TwitterUser.objects.get(id=id)
    request.user.twitteruser.follow.remove(follow_user)
    return HttpResponseRedirect(reverse('profile_view', kwargs={'id': id}))


def unfollow_user(request, id):
    unfollow_user = TwitterUser.objects.get(id=id)
    request.user.twitteruser.follow.remove(unfollow_user)
    return HttpResponseRedirect(reverse('profile_view', kwargs={'id': id}))
