from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_Topic(request):
    ELTO=TopicForm()
    d={'ELTO' : ELTO}
    if request.method=='POST':
        TLDO=TopicForm(request.POST)
        if TLDO.is_valid():
            TLDO.save()
            return HttpResponse('Topic created')
    return render(request,'insert_Topic.html',d)


def insert_WebPage(request):
    ELWO=WebPageForm()
    d={'ELWO' : ELWO}
    if request.method=='POST':
        WLDO=WebPageForm(request.POST)
        if WLDO.is_valid():
            WLDO.save()
            return HttpResponse('WebPage created')
    return render(request,'insert_WebPage.html',d)



def insert_AccessRecord(request):
    ELAO=AccessRecordForm()
    d={'ELAO' : ELAO}
    if request.method=='POST':
        ALDO=AccessRecordForm(request.POST)
        if ALDO.is_valid():
            ALDO.save()
            return HttpResponse('AccessRecord created')
    return render(request,'insert_AccessRecord.html',d)