from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.registeration_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('update/', views.update_view, name="update")
]
