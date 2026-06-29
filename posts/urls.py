from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.landing,
        name='landing'
    ),

    path(
        'home/',
        views.home,
        name='home'
    ),

    path(
        'like/<int:id>/',
        views.like_post,
        name='like_post'
    ),

    path(
        'comment/<int:id>/',
        views.add_comment,
        name='add_comment'
    ),

    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),
    path(
        'follow/<str:username>/',
        views.follow_user,
        name='follow_user'
    ),
    path(
        'messages/',
        views.messages_page,
        name='messages'
    ),

    path(
        'groups/',
        views.groups_page,
        name='groups'
    ),

    path(
        'notifications/',
        views.notifications_page,
        name='notifications'
    ),

    path(
        'settings/',
        views.settings_page,
        name='settings'
    ),
]
