from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from FormApp.models import Createadmin
from FormApp.models import Group
from FormApp.models import Location
from FormApp.models import Student


#Create your views here.
def login(request):
    return render(request,'login.html')
   
def check(request):
    na=request.POST.get('username')
    pa=request.POST.get('password')
    if Createadmin.objects.filter(username=na,password=pa).exists():
        return redirect('index')
    else:
        return HttpResponse('Invalid Credentials')


def index(request):
    gi=Group.objects.all()
    li=Location.objects.all()
    si=Student.objects.all()
    return render(request,'index.html',{'gi':gi,'li':li,'si':si})


def main(request):
    if request.method == 'POST':    
        gp=request.POST.get('gname')
        ln=request.POST.get('lname')
        sn=request.POST.get('sname')
        data=Student(groupname=gp,locationname=ln,studentname=sn)
        data.save()
        if Student.objects.filter(groupname=gp,locationname=ln,studentname=sn).exists():
             return redirect('register')
        else:
            return HttpResponse("INVALID DATA")

    

def register(request):
    return render(request,'fillform.html')

def fill(request,dataid):
    if request.method == 'POST':
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        pn=request.POST.get('pname')
        em=request.POST.get('email')
        re=request.POST.get('remarks')
        Student.objects.filter(id=dataid).update(first_name=fn,last_name=ln,parent_name=pn,email=em,remarks=re)
        return redirect('index')
    
    return HttpResponse("INVALID DATA")

   
def login(request):
    return render(request,'login.html')

def adgroup(request):
    return render(request,'addgroup.html')

def saveAdgroup(request):
    if request.method=='POST':
        gid=request.POST.get('groupid')
        gname=request.POST.get('groupname')
        gd=Group(group_id=gid,group_name=gname)
        gd.save()
    return redirect('adgroup')

def adlocation(request):
    if request.method=='POST':
        lid=request.POST.get('locationid')
        lname=request.POST.get('locationname')
        ld=Location(location_id=lid,location_name=lname)
        ld.save()
    return render(request,'adlocation.html')

def adstudent(request):
    d=Group.objects.all()
    l=Location.objects.all()
    return render(request,'adstudent.html',{'d':d,'l':l})

def savestudent(request):
    if request.method=='POST':
        sname=request.POST.get('studentname')
        gname=request.POST.get('groupname')
        lname=request.POST.get('locationname')
        sl=Student(studentname=sname,groupname=gname,locationname=lname)
        sl.save()
    return redirect('adstudent')




