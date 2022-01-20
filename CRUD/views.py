from django.shortcuts import render

# Create your views here.

def CRUD_VIEW(request):
    return render(request, 'CRUD/index.html')


