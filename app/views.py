from django.shortcuts import render

# Create your views here.
def load_img(request):
    return render(request,'page.html')