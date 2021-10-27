from django.shortcuts import redirect, render
from .models import InterestMsg


def index(request):
    msg = False
    msgHead = ''
    msgSubject = ''
    msgBody = ''
    if request.method == 'POST':
        msges = InterestMsg.objects.all()
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']

        for items in msges:
            if items.name == name or items.email == email:
                msg = True
                msgHead = 'Already sent!'
                msgSubject = 'We will get back to you pretty soon.'
            else:
                userMsg = InterestMsg.objects.create(
                    name=name, email=email, message=msg)
                userMsg.save()
                msg = True
                msgHead = 'Thank You!'
                msgSubject = 'We are happier with your interest'
                msgBody = 'for our reply and stay connected'
    return render(request, template_name='index.html', context={
        'msg': msg,
        'msgHead': msgHead,
        'msgbody': msgBody,
        'msgSubject': msgSubject
    })


def contact(request):

    return render(request, template_name='contact.html')
# Create your views here.
