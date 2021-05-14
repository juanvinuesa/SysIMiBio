from django.shortcuts import render

# Create your views here.
def bioblitz(request):
    return render(request, 'index.html')