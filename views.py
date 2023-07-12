from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.hashers import check_password,make_password
from rest_framework import routers, serializers, viewsets
from .serializer import registrationSerializer

# Create your views here.
def index(request):
    if request.method == 'POST':
        fir_name=request.POST.get('fnamee')
        las_name=request.POST.get('lnamee')
        # print(fir_name,'...',las_name)
        c_obj = registration(
            first_name=fir_name,
            last_name=las_name
        )
        c_obj.save()

    # fetch_obj = registration.objects.all()
    # fetch_obj = registration.objects.filter(first_name='hemraj')
    # fetch_obj = registration.objects.get(first_name='hemraj') throw error
    # fetch_obj = registration.objects.get(first_name='pratyush')
    

    # obj_cls = registration{
    #     first_name=fir_name,
    #     last_name=las_name
    # }
    # obj_cls.save()

    # return render(request,'home.html',{'key':fetch_obj})
    return render(request,'home.html')
def cont(request):
    return render(request,'contact.html')

def signup(request):
    if request.method == 'POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('gender')

        c_obj = registration(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = make_password(password),
            mobile = mobile,
            gender = gender
        )

        c_obj.save()
        return redirect('home')
def login(request):
    if request.method=='POST':
        email1= request.POST.get('emailbox')
        pswd=request.POST.get('pswd')
     
    try:
        fetch_email = registration.objects.get(email=email1)

        if check_password(pswd,fetch_email.password):
            request.session['name'] = fetch_email.first_name
            return redirect('home')
        else:
            return HttpResponse('wrong password')
    except:
        return HttpResponse('entered email do not exist')
    
def logout(request):
    request.session.clear()
    return redirect('home')

class registrationViewSet(viewsets.ModelViewSet):
    queryset = registration.objects.all()
    serializer_class = registrationSerializer