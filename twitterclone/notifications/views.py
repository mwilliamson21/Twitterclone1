from django.shortcuts import render
from twitterclone.notifications.model import Notifications
from contrib.auth.decorators import login_required
from twitterclone.twitteruser.models import TwitterUser


@login_required
def view_notification(request, id):
    html = 'notifications.html'
    twitteruser = TwitterUser.objects.filter(user=request.user).first()
    notifications = Notifications.objects.filter(username=twitteruser)

    for n in notifications:
        n.delete()
    return render(request, html, {'notifications': notifications})
