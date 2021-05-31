from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Designation(models.Model):
    role=models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.role



GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
)
COURSE_CHOICES = (
    ('B.Tech', 'Bachelor of technology'),
    ('MBA', "Master of bussiness Administration"),
    ('MCA', 'Master of computer Applications'),
    ('DEGREE', 'B.com computers'),
    ('CA', 'Charted Accountant'),
)


class Empregistration(models.Model):
    """Emp registration Here"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES, default=None)
    qualification = models.CharField(max_length=100)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    is_approved = models.BooleanField(default=False)

    objects=models.Manager()

    def __str__(self):
        return self.name


class Empdetails(models.Model):
    """Employee details Here"""
    user= models.OneToOneField(User, related_name="emp_info", on_delete=models.CASCADE, )
    empname= models.OneToOneField(Empregistration,related_name='employee',on_delete=models.CASCADE, )
    experience = models.CharField(max_length=10)
    salary=models.IntegerField()
    profile_pic = models.ImageField('pictures/')
    mobile = models.IntegerField()
    age=models.IntegerField()
    address = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return str(self.empname)



class Team(models.Model):
    """teams information here"""
    team_name=models.CharField(max_length=100)
    team_members=models.ForeignKey(Empdetails,related_name='team_members',on_delete=models.CASCADE,)
    team_lead=models.ForeignKey(Empdetails,on_delete=models.CASCADE,)
    #project_name=models.ForeignKey(Project,on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return str(self.team_name)


class Mailinbox(models.Model):
    """Mail related data here"""
    sender=models.ForeignKey(Empdetails,related_name='senders',on_delete=models.CASCADE,)
    receiver= models.ForeignKey(Empdetails,related_name='receiver',on_delete=models.CASCADE, )
    subject=models.TextField(max_length=100)
    body=models.TextField(max_length=200)
    file=models.FileField(upload_to="media/",null=True,blank=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.sender)

class Project(models.Model):
    """Project deatls Here"""
    project=models.CharField(max_length=100)
    team_name=models.ForeignKey(Team,on_delete=models.CASCADE,)

    objects=models.Manager()

    def __str__(self):
        return self.project_name


