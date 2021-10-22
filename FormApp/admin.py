from django.contrib import admin
from FormApp.models import Createadmin
from FormApp.models import Group
from FormApp.models import Location
from FormApp.models import Student
from import_export.admin import ImportExportModelAdmin

#Register your models here.
admin.site.register(Createadmin)
@admin.register(Group)
class grp(ImportExportModelAdmin):
    pass
admin.register(Group)
@admin.register(Location)
class lrp(ImportExportModelAdmin):
    pass
admin.register(Location)
@admin.register(Student)
class srp(ImportExportModelAdmin):
    pass
admin.register(Student)

