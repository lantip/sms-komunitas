from django import forms
from member.models import Usia, StatusSosial

class AgeForm(forms.ModelForm):
    error_css_class = 'alert alert-error'
    
    class Meta:
        model = Usia
        fields = ['name', 'umur_min', 'umur_max']
        
class StatusSosialForm(forms.ModelForm):
    error_css_class = 'alert alert-error'
    
    class Meta:
        model = StatusSosial
        fields = ['name', 'score_min', 'score_max']

class SearchForm(forms.Form):
    q = forms.CharField(required=False)