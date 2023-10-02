from django.shortcuts import render
from base.views.authentication import loginpage, logoutUser, registerpage
from base.views.rooms import home, room, createRoom, updateRoom, deleteRoom
from base.views.user_profile import userProfile, updateUser
from base.views.topics import topicsPage
from base.views.activity import activityPage
from django.urls import path

# Include the views in your URL patterns
urlpatterns = [
    # Authentication views
    path('login/', loginpage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerpage, name='register'),

    # Rooms views
    path('home/', home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<int:pk>/', updateRoom, name='update-room'),
    path('delete-room/<int:pk>/', deleteRoom, name='delete-room'),

    # User profile views
    path('user-profile/<int:pk>/', userProfile, name='user-profile'),
    path('update-user/', updateUser, name='update-user'),

    # Topics views
    path('topics/', topicsPage, name='topics'),

    # Activity view
    path('activity/', activityPage, name='activity'),
]







