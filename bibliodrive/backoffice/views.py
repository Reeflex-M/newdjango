from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Implement your home page logic here
    return render(request, 'home.html')  # Assuming you have a template called 'home.html'

def test(request):
    html = "<html><body>TRY</body></html>"
    return HttpResponse(html)

def hello(request,nom="toto"):
    html = f"<html><body>Hello {nom}</body></html>"
    return HttpResponse(html)
