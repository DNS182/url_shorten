from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from shorted.models import Shortner
from url_short.settings import BASE_DIR
from .forms import ShortnerForm
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def index(request):
    BASE_URL = get_current_site(request) #THIS IS OUR CURRENT SITE
    if request.method == 'POST':
        form = ShortnerForm(request.POST)
        if form.is_valid():
            form.save()
            key = form.cleaned_data.get('key') #getting value from html field and assigning it to key. 
            messages.success(request, f"URL has been successfully shortened to {BASE_URL}/{key}")
            return redirect('index')

    else:
        form = ShortnerForm()

    return render(request , 'index.html' ,{'form' : form})


#this is the key view to redirect shortened url to original url.
def redirector(request , key):
    barca = get_object_or_404(Shortner , key = key)
    return redirect(barca.origna_url)
