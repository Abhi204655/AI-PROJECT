from django.contrib import admin
from .models import (profile, Loans, VisitedLoan)


class VisitedAdmin(admin.ModelAdmin):
    list_display = ('user', 'visitedLoanId', 'timevisited')
    readonly_fields = ('timevisited',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(profile)
admin.site.register(Loans)
admin.site.register(VisitedLoan, VisitedAdmin)
