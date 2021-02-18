from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, "home.html", {})


def contact_view(request):
    my_context = {
        "my_text": "This is my contacts page",
        "my_number": 123,
        "my_list": [223, 3345, 34343, 324, 11, "ABC"]
    }
    return render(request, "contact.html", my_context)
