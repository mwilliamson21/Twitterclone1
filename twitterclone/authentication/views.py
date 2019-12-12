"""twitterclone1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitterclone.authentication.forms import LoginForm, UserAdd
from django.contrib.auth.models import User
from twitterclone.twitterusers.models import TwitterUser


def login_view(request):
    html = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:

                login(request, user)
            else:
                HttpResponseRedirect(reverse('login'))
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )

    form = LoginForm()

    return render(request, html, {'form': form})


def createuser(request):
    html = 'signup.html'
    if request.method == 'POST':
        form = UserAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
        new_user = TwitterUser.objects.create(
            user=user,
            name=data['username']
        )
        new_user.following.add(new_user)
        return HttpResponseRedirect(reverse('homepage'))
    form = UserAdd()
    return render(request, html, {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
