from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World </h1>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [23, 389, 43],
    }
    return render(request, "about.html", my_context)
