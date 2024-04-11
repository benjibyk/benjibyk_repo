from django.urls import path
from uApp import views  # Adjust the import statement as needed
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('submit_url/', views.submit_url, name='submit_url'), 
    path('shortened_url/<str:short_url>/', views.shortened_url, name='shortened_url'),  # Include the parameter in the URL pattern
]
