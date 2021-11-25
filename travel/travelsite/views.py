from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Destination,book

superusers = User.objects.filter(is_superuser=True)

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            if user in superusers:
                auth.login(request, user)
                return redirect("admin")
            else:
                auth.login(request, user)
                return redirect("index")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('index')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')

def book_now(request):
    if request.method=='POST':
        From = request.POST['From']
        to = request.POST['To']
        name = request.POST['name']
        start = request.POST['Start_date']
        end = request.POST['end_date']
        Book = book.objects.create(From=From,To=to,name=name,Start_date=start,end_date=end)
        Book.save()
    return render(request,'book_now.html')


def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})

def upcoming(request):
    name = auth.get_user(request).username
    upcome = book.objects.filter(name = name)
    return render(request,'upcoming.html',{'upcome' : upcome})

def remove(request,id):
    item = book.objects.get(id=id)
    item.delete()
    name = auth.get_user(request).username
    upcome = book.objects.filter(name = name)
    return render(request,'upcoming.html',{'upcome':upcome})

def admin(request):
    upcome = book.objects.all()
    return render(request,'admin.html',{'upcome' : upcome})

def logout(request):
    
    auth.logout(request)
    return render(request,'login.html')

def decline(request,id):
    item = book.objects.get(id=id)
    item.delete()
    upcome = book.objects.all()
    return render(request,'admin.html',{'upcome':upcome})