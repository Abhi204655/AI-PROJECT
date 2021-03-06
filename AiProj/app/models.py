from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=140, null=True)
    lastName = models.CharField(max_length=140, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.user.username


class Loans(models.Model):

    Loantypes = (
        ("HM", "Home"),
        ("PR", "Personal"),
        ("BS", "Bussiness")
    )

    bank = models.CharField(max_length=200)
    type = models.CharField(max_length=100, null=True, choices=Loantypes)
    amount = models.IntegerField()
    interest = models.IntegerField()
    content = models.TextField(null=True)

    def __str__(self):
        return self.bank + ' - ' + str(self.amount) + ' - ' + self.type


class VisitedLoan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visitedLoanId = models.IntegerField()
    timevisited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' - ' + str(self.visitedLoanId)
