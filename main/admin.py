from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . models import BanksNew
# Register your models here.
#admin.site.register(BankBranches)
admin.site.register(BanksNew)
class BanksNewAdmin(ImportExportModelAdmin):
	pass