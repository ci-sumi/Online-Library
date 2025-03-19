from django.shortcuts import render

# Create your views here.
def index(request):
    print("Index view is being called!")
    return render(request,'index.html')