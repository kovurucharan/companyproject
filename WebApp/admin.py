from django.contrib import admin

# Register your models here.
from WebApp.models import Empregistration,Empdetails,Team,Designation,Project,Mailinbox

admin.site.register(Empregistration)
admin.site.register(Empdetails)
admin.site.register(Designation)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Mailinbox)