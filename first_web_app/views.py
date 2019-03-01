from random import randint
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('home')

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
