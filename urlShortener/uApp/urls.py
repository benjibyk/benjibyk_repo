from django.urls import path
from uApp import views

urlpatterns = [
    # Other URL patterns...
    path('shortened_url/<str:short_url>/', views.shortened_url, name='shortened_url'),
]
