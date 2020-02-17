from django.shortcuts import render,redirect
from django.http import HttpResponse
from appecom.forms import *
from appecom.models import *

# Create your views here.
def home(request):
    catlist=Category.objects.all()
    Productlist=Product.objects.all()
    context={'categorylist':catlist,'productlist':Productlist}
    return render(request,"home.html",context)

def Catform(request):
    catform = Categoryform
    try:
        if request.method == 'POST':
            catform=Categoryform(request.POST)
            if catform.is_valid:
                catform.save()
                redirect("/")
    except:
        return HttpResponse("this category is already registered")

    return render(request,"categoryform.html", {'form':catform})

def Uform(request):
    usrform = Userform
    if request.method == 'POST':
        print(request.POST, request.FILES)
        usrform=Userform(request.POST, request.FILES)
        if usrform.is_valid:
                usrform.save()
                return redirect("/")
    return render(request,"userform.html", {'form':usrform})

def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        log=User.objects.get(Email=email)

        if email==log.Email and password==log.Password:
            request.session['Username']=log.Name
            return redirect("/home")
        else:
            return render(request,"login.html",{'im':"Invalid Username and password"})
    except:
        return render(request,"login.html",{'lm':"Invalid Username and password"})

    return render(request,"login.html")

def logout(request):
    try:
        ls=list(request.session.keys())
        for i in ls:
            del request.session[i]
    except:
        pass
    return redirect("/login")

# Product form
def Pform(request):
    form=Productform
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form=Productform(request.POST, request.FILES)
        if form.is_valid:
                form.save()
                return redirect("/")
    context={'form':form}
    return render(request,'productform.html',context)

def updateproduct(request,pk):
    product = Product.objects.get(id=pk)
    print(product)
    form = Productform(instance=product)
    if request.method=='POST':
        print("Printing :",request.POST)
        form=Productform(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("/")

    context={'form':form}
    return render(request, 'productform.html',context)

def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    if request.method=='POST':
        product.delete()
        return redirect("/")
    context={'item':product}
    return render(request,"delete.html",context)

def cart(request):
    return render(request,'cart.html')


        
 





    



