from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profilePage, name="profile"),
    path('profile/update', views.updateProfile, name="update"),
    path('loans', views.loans, name="loans"),
    path('loans/<int:pk>', views.loanDetail, name="loanDetail")
]
