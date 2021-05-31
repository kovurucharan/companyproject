from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from WebApp.forms import EmpregistrationForm,DesignationForm,TeamForm,ProjectForm,MailinboxForm
from  WebApp import forms
from WebApp.models import Empdetails,Empregistration,Team,Project,Mailinbox
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    """welcome to home page"""
    return render(request,'MyApp/home.html')
def thanks(request):
    return render(request,'MyApp/thanks.html')


def designation(request):
    """TO save the all the designations in the organisation"""
    if request.method == "POST":
        form = forms.DesignationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/th/')

    else:
        form =forms.DesignationForm()
    return render(request, 'MyApp/designation.html', {'form': form})


def empregister(request):
    """employee register page here"""
    form=forms.EmpregistrationForm()
    return render(request,'MyApp/empregister.html',{'form':form})

def empsave(request):
    """save employee registration"""
    if request.method=='POST':
        form=forms.EmpregistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/details/')
    else:
        form=forms.EmpregistrationForm()
    return render(request,'MyApp/empregister.html',{'form':form})

# def empdetails(request):
#     form=forms.EmpdetailsForm()
#     return render(request,'MyApp/empdetails.html',{'form':form})
def empdetails(request):
    return render(request,'MyApp/empdetails.html')

def detailssave(request):
    """here save empdetails """
    if Empregistration.objects.filter(email=request.POST["email"],is_approved=True).exists():
        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'])
        empname=Empregistration.objects.get(email=request.POST['email'])
        Empdetails.objects.create(user=user,
                                     empname=empname,
                                     mobile=request.POST['mobile'],
                                     profile_pic=request.FILES['profile_pic'],
                                     salary=request.POST['salary'],
                                     experience=request.POST['experience'],
                                     age=request.POST['age'],
                                     address=request.POST['address'])
        return HttpResponseRedirect('/elist/')
    else:
        return HttpResponse("Not Valid user")

def user_login(request):
    """user login page"""
    return render(request, 'MyApp/login.html')

def login_verify(request):
    """before login to verify the user exists are not"""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if Empdetails.objects.filter(user=user).exists():
            return HttpResponseRedirect('/elist/')
        else:
            return render(request, 'MyApp/home.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'MyApp/home.html', {'error': 'Invalid username or password'})


def logout_page(request):
    """logout employee here"""
    logout(request)
    return HttpResponseRedirect('/ulogin/')



def emplist(request):
    """total employees in the company"""
    obj=Empdetails.objects.all()
    return render(request,'MyApp/emplist.html',{'obj':obj})

def employee_details(request,id=None):
    """employee details here"""
    jk=Empdetails.objects.get(id=id)
    return render(request,'MyApp/employeedetails.html',{'obj':jk})

def team(request):
    """team details here"""
    form=forms.TeamForm()
    return render(request,'MyApp/teams.html',{'form':form})

def teamsave(request):
    """team svae details here"""
    if request.method=='POST':
        form=forms.TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/th/')
    else:
        form=forms.EmpregistrationForm()
    return render(request,'MyApp/teams.html',{'form':form})

def total_teams(request):
    """total teams in company here"""
    tt=Team.objects.all()
    return render(request,'MyApp/teamslist.html',{'obj':tt})

def project(request):
    """project details """
    form=forms.ProjectForm()
    return render(request,'MyApp/project.html',{'form':form})

def projectsave(request):
    """projects save here"""
    if request.method=='POST':
        form=forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/th/')
    else:
        form=forms.ProjectForm()
    return render(request,'MyApp/project.html',{'form':form})

def total_projects(request):
    tp=Team.objects.all()
    return render(request,'MyApp/projectlist.html',{'tp':tp})


def mail(request):
    """To send email from one employee to another"""
    if request.method == "POST":
        form =forms.MailinboxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/th/')
        else:
            return HttpResponse("invalid")
    else:
        form =forms.MailinboxForm()
        return render(request, "MyApp/mail.html", {'form': form})







