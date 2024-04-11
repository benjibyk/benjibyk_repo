from django import forms

class URLShortenForm(forms.Form):
    original_url = forms.URLField(label='Enter URL', max_length=200)

