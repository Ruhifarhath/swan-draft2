from django.shortcuts import render

# Create your views here.

def firstView(request):
    return render(request,'swanapp/index.html')
