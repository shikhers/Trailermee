from django.shortcuts import render
from . models import Video,Hollywood,Bollywood,Cartoon

def MainView(request):
    videos = Video.objects.order_by('-date_added')
    context = {'videos':videos}
    return render(request, 'main.html',context)

def Hollyview(request):
    hollmodel = Hollywood.objects.order_by('-date_added')
    context = {'hollmodel':hollmodel}
    return render(request,'hollywood.html',context)


def Bollyview(request):
    bollymodel = Bollywood.objects.order_by('-date_added')
    context = {'bollymodel':bollymodel}
    return render(request,'bollywood.html',context)

def Cartoonview(request):
    carmodel = Cartoon.objects.order_by('-date_added')
    context = {'carmodel':carmodel}
    return render(request,'cartoon.html',context)
