from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is for signing with google function....")

def register_user(request):
    return render(request, 'index.html')
