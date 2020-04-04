from django.contrib import admin
from .models import (profile, Loans, VisitedLoan)

admin.site.register(profile)
admin.site.register(Loans)
admin.site.register(VisitedLoan)
