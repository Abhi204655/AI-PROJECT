from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import profile
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"app/index.html")

@login_required(login_url="account/login")
def profilePage(request):
    try:
        pro=profile.objects.get(user=request.user)
    except profile.DoesNotExist:
        return render(request,"app/profile.html",{"updated" : False})
    return render(request,"app/profile.html",{"profile" : pro,"updated":True})


@login_required(login_url="account/login")
def updateProfile(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        image = request.FILES['image']
        dob = request.POST['dob']
        address = request.POST['address']
        city = request.POST['city']
        pin = request.POST['pin']
        state = request.POST['state']
        country = request.POST['country']
        employed = request.POST['employed']
        salary = request.POST['salary']
        credit = request.POST['credit']
        dependency = request.POST['dependency']
        if firstName=='' or lastName=='' or dob=='' or address=='' or city=='' or pin=='' or state=='' or country=='' or employed=='' or salary=='' or credit=='' or dependency=='':
            messages.warning(request,"Please fill all the fields!!!")
            return render(request,"app/update.html")
        pro = profile(user = request.user,firstName=firstName,lastName=lastName,image=image,dob=dob,address=address,city=city,pin=pin,state=state,country=country,employed=employed,salary=salary,credit=credit,dependency=dependency)
        pro.save()
        return render(request,"app/profile.html",{"profile" : pro,"updated":True})
    else:
        return render(request,"app/update.html")