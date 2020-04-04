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
        queryset = VisitedLoan.objects.filter(user=request.user)
        data = []
        count = 0
        for query in queryset:
            if count == 3:
                break
            try:
                temp = Loans.objects.get(id=query.visitedLoanId)
                count += 1
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
        return render(request, "app/profile.html", {"profile": pro, "updated": True})
    else:
        return render(request, "app/update.html")


def loans(request):
    data = Loans.objects.all()
    context = {
        'loans': data
    }
    queryset = VisitedLoan.objects.filter(user=request.user)
    data = []
    for query in queryset:
        try:
            temp = Loans.objects.get(id=query.visitedLoanId)
            data.append(temp)
        except Loans.DoesNotExist:
            continue

    context['recommended'] = data
    return render(request, 'app/loans.html', context)


def loanDetail(request, pk):
    try:
        data = Loans.objects.get(id=pk)
        try:
            ele = VisitedLoan.objects.get(
                user=request.user, visitedLoanId=data.id)
        except VisitedLoan.DoesNotExist:
            visit = VisitedLoan(user=request.user, visitedLoanId=data.id)
            visit.save()
    except Loans.DoesNotExist:
        return redirect("/")
    context = {'data': data}
    return render(request, "app/loanDetail.html", context)
