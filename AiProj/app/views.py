from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import profile, Loans, VisitedLoan
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "app/index.html")


@login_required(login_url="account/login")
def profilePage(request):
    try:
        pro = profile.objects.get(user=request.user)
        queryset = VisitedLoan.objects.filter(
            user=request.user).order_by('-timevisited')
        data = []
        for query in queryset:
            try:
                temp = Loans.objects.get(id=query.visitedLoanId)
                data.append(temp)
            except Loans.DoesNotExist:
                continue
    except profile.DoesNotExist or VisitedLoan.DoesNotExist:
        return render(request, "app/profile.html", {"updated": False})
    return render(request, "app/profile.html", {"profile": pro, "updated": True, "loans": data})


@login_required(login_url="account/login")
def updateProfile(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        image = request.FILES['image']
        if firstName == '' or lastName == '':
            messages.warning(request, "Please fill all the fields!!!")
            return render(request, "app/update.html")
        pro = profile(user=request.user, firstName=firstName,
                      lastName=lastName, image=image)
        pro.save()
        messages.success(request, "Profile updated successfully...")
        return render(request, "app/profile.html", {"profile": pro, "updated": True})
    else:
        return render(request, "app/update.html")


def loans(request):
    home = Loans.objects.filter(type="HM")
    bussiness = Loans.objects.filter(type="BS")
    personal = Loans.objects.filter(type="PR")
    context = {
        'homeloans': home,
        'bussinessloans': bussiness,
        'personalloans': personal
    }
    queryset = VisitedLoan.objects.filter(
        user=request.user).order_by('-timevisited')
    data = []
    for query in queryset:
        try:
            temp = Loans.objects.get(id=query.visitedLoanId)
            data.append(temp)
        except Loans.DoesNotExist:
            continue

    context['recommended'] = data[:3]
    return render(request, 'app/loans.html', context)


def loanDetail(request, pk):
    try:
        data = Loans.objects.get(id=pk)
        try:
            ele = VisitedLoan.objects.get(
                user=request.user, visitedLoanId=data.id)
            ele.delete()
        except VisitedLoan.DoesNotExist:
            pass
        visit = VisitedLoan(user=request.user, visitedLoanId=data.id)
        visit.save()
    except Loans.DoesNotExist:
        return redirect("/")
    context = {'data': data}
    return render(request, "app/loanDetail.html", context)
