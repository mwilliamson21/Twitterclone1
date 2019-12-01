from django.urls import path
from twitterclone.tweets import views


urlpatterns = [

    path('', views.viewhomepage, name='homepage'),
    path('tweet/<int:id>/', views.view_tweet, name='view_tweets'),
    path('maketweets/', views.make_tweets),

]
