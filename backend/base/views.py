from django.shortcuts import render

# Create your views here.
def home(request):
    context = {} # context is for like variables to be passed in from schema
    return render(request, 'base/home.html', context)
