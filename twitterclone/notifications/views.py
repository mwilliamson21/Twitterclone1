from django.shortcuts import render
from twitterclone.notifications.models import Notifications
from django.contrib.auth.decorators import login_required
from twitterclone.twitterusers.models import TwitterUser


@login_required
def view_notification(request):
    html = 'notifications.html'
    twitteruser = TwitterUser.objects.filter(user=request.user).first()
    notifications = Notifications.objects.filter(twitter_user=twitteruser)

    for n in notifications:
        n.delete()
    return render(request, html, {'notifications': notifications})
