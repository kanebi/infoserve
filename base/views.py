from django.shortcuts import render


def index(request):

    return render(request, template_name='index.html')
def contact(request):

    return render(request, template_name='contact.html')
# Create your views here.
def services(request):

    return render(request, template_name='services.html')
# Create your views here.
