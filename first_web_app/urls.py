"""first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def home_page(request):
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio(request):
    image_url =[]
    for i in range(5):
        random_number = randint(0,100)
        image_url.append("https://picsum.photos/400/600/?image={}".format(random_number))

    context = {'gallery_image': image_url}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request):
    context = {'skills': ["a", "b", "c"], 'interests':["e", "f", "g"]}
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def fave_links(request):
    fave = ["www.google.com", "www.facebook.com", "www.instagram.com"]
    context = {'links': fave }
    response = render(request, 'fave_links.html', context)
    return HttpResponse(response)


urlpatterns = [
    path('home', home_page),
    path('portfolio/', portfolio),
    path('about/', about_me),
    path('favlinks/', fave_links)
]
