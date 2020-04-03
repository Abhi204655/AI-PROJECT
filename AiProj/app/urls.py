from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.home,name="home"),
    path('profile',views.profilePage,name="profile"),
    path('profile/update',views.updateProfile,name="update")
]
