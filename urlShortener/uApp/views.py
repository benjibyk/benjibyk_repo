# views.py

import hashlib
from django.shortcuts import render, redirect
from django.core.exceptions import MultipleObjectsReturned
from .models import ShortenedURL

def submit_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_url = generate_short_url(original_url)
        try:
            # Save the original and shortened URLs to the database
            ShortenedURL.objects.create(original_url=original_url, short_url=short_url)
            # Redirect to the shortened URL page with the short URL
            return redirect('shortened_url', short_url=short_url)
        except MultipleObjectsReturned:
            # Handle the case where multiple objects are returned for the same short URL
            # Redirect to an error page or display a message to the user
            return render(request, 'error.html', {'message': 'Short URL already exists'})
    return render(request, 'submit_url.html')

def shortened_url(request, short_url):
    # Retrieve the first ShortenedURL object associated with the short URL from the database
    shortened_url_obj = ShortenedURL.objects.filter(short_url=short_url).first()
    return render(request, 'shortened_url.html', {'short_url': shortened_url_obj})


def generate_short_url(original_url):
    # Generate SHA-256 hash of the original URL
    hash_object = hashlib.sha256(original_url.encode())
    hash_digest = hash_object.hexdigest()
    # Extract first 8 characters of the hash to create short URL
    short_url = hash_digest[:8]
    return short_url

def index(request):
    return render(request, 'index.html')
