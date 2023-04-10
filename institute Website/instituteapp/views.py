from django.shortcuts import render
from .models import feedbackdata
from .models import coursedata
from .models import reviews

def homepage(request):
    return render(request,'homepage.html')

def contactpage(request):
    if request.method=='GET':
        return render(request,'contactpage.html')
    else:
        feedbackdata(
            name=request.POST.get("name"),
            mail=request.POST.get("email"),
            subject=request.POST.get("subject"),
            messange=request.POST.get("message")
        ).save()
        return render(request,'contactpage.html')

def servicespage(request):
    course=coursedata.objects.all()
    return render(request,'servicespage.html',{'course':course})

def feedbackpage(request):
    if request.method=='GET':
        feedbk=reviews.objects.all().values()
        return render(request,'feedbackpage.html',{'feedbk':feedbk})
    else:
        reviews(
            name=request.POST.get("Name"),
            ratings=request.POST.get("Rating"),
            comments=request.POST.get("Comment")
        ).save()
        feedbk=reviews.objects.all().values()
        return render(request,'feedbackpage.html',{'feedbk':feedbk})

def gallarypage(request):
    return render(request,'gallarypage.html')


    
