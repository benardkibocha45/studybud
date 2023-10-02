from django.urls import path
from .views import authentication, rooms, user_profile, topics, activity

urlpatterns = [
    path('login/', authentication.loginpage, name="login"),
    path('logout/', authentication.logoutUser, name="logout"),
    path('register/', authentication.registerpage, name="register"),

    path('', rooms.home, name="home"),
    path('room/<str:pk>/', rooms.room, name="room"),
    path('profile/<str:pk>/', user_profile.userProfile, name="user-profile"),

    path('create-room/', rooms.createRoom, name="create-room"),
    path('update-room/<str:pk>/', rooms.updateRoom, name="update-room"), 
    path('delete-room/<str:pk>/', rooms.deleteRoom, name="delete-room"),  
    path('delete-message/<str:pk>/', rooms.deleteMessage, name="delete-message"), 

    path('update-user/', user_profile.updateUser, name="update-user"),
    path('topics/', topics.topicsPage, name="topics"),
    path('activity/', activity.activityPage, name="activity"),
]
