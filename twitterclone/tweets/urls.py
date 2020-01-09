from django.urls import path
from twitterclone.tweets import views


urlpatterns = [

    path('', views.ViewHomePage.as_view(), name='homepage'),
    path('tweet/<int:id>/', views.ViewTweet.as_view(), name='view_tweet'),
    path('maketweets/', views.make_tweets),

]
