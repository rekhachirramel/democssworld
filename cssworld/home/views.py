from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home1.html")
def project(request):
    return render(request,"projects.html")
def contact(request):
    return render(request,"contact.html")
