from django.shortcuts import render


def index(request):
    print('hello world')
    return render(request, template_name='index.html')
# Create your views here.
