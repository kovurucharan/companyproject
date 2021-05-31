from  WebApp.models import Empregistration,Empdetails,Team,Designation,Project,Mailinbox

from django import  forms

class EmpregistrationForm(forms.ModelForm):
    class Meta:
        model=Empregistration
        fields='__all__'

class DesignationForm(forms.ModelForm):
    class Meta:
        model=Designation
        fields='__all__'

class TeamForm(forms.ModelForm):
    """team model form here"""
    class Meta:
        model=Team
        fields='__all__'

class ProjectForm(forms.ModelForm):
    """project model form here"""
    class Meta:
        model=Project
        fields='__all__'

class MailinboxForm(forms.ModelForm):
    class Meta:
        model=Mailinbox
        fields='__all__'