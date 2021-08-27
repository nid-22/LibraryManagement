from django import forms
from Users.models import Users

class registerForm(forms.ModelForm):
    Gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=Users.GENDER_CHOICES,required=False)
    
    class Meta:
        model=Users
        fields = '__all__'

class userUpdateForm(forms.ModelForm):
    Gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=Users.GENDER_CHOICES)
    class Meta:
        model=Users
        fields = ['Name','Address','Gender','email','BirthDate','Phone']
    