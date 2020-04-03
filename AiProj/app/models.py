from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=140,null=True)
    lastName = models.CharField(max_length=140,null=True)
    image = models.ImageField(upload_to='images/',null=True)
    dob = models.DateField(blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    pin = models.IntegerField()
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    employed = models.CharField(max_length=150)
    salary = models.IntegerField(null=True)
    credit = models.IntegerField(null=True)
    dependency = models.IntegerField(null=True)


    def __str__(self):
        return self.user.username

class Loans(models.Model):
    bank = models.CharField(max_length=200)
    amount = models.IntegerField()
    interest = models.IntegerField()
    emi = models.IntegerField()

    def __str__(self):
        return self.bank + ' - ' +  str(self.amount)
    

    