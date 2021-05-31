
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('designation/',views.designation),
    path('register/',views.empregister),
    path('th/',views.thanks),
    path('empsave/',views.empsave),
    path('details/',views.empdetails),
    path('detailsave/',views.detailssave),
    path('ulogin/',views.user_login),
    path('loginverify/',views.login_verify),
    path('elist/',views.emplist),
    path('empdetails/<int:id>/',views.employee_details),
    path('teams/',views.team),
    path('teamsave/',views.teamsave),
    path('teamlist/',views.total_teams),
    path('project/',views.project),
    path('projectsave/',views.projectsave),
    path('plist/',views.total_projects),
    #path('mail/',views.mails),
    #path('mailsave/',views.mailsave),
    path('mail/',views.mail),


]