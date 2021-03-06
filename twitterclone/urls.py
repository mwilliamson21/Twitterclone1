"""test_project URL Configuration

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

from django.contrib import admin
from django.urls import path
from twitterclone.authentication.urls import urlpatterns as auth_urls
from twitterclone.notifications.urls import urlpatterns as notif_urls
from twitterclone.tweets.urls import urlpatterns as tweet_urls
from twitterclone.twitterusers.urls import urlpatterns as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/', signup, name='signup'),
    # path('addtweet/', addtweetview),
    # path('addauthor/', addauthorview),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('error/', errorpage, name='error')
    
]
urlpatterns += auth_urls
urlpatterns += notif_urls
urlpatterns += tweet_urls
# urlpatterns += profile_urls
urlpatterns += user_urls
