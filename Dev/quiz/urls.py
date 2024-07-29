from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('quiz' , views.login_page , name='login_page' ),
]
