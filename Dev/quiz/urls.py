from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing_page'),
    path('login/' , views.login_view , name='login_page' ),
    path('signup/' , views.signup_view , name='signup_page'),
    path('home/' , views.home_view , name='home_page'),
    path('logout/' , views.logout_view , name='logout'),
    path('profile/' , views.profile_view , name='profile')
]
