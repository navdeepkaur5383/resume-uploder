from django import forms
from .models import Resume

gender_choices=[('Male','Male'),("Female","Female")]
job_city=[('Ludhiana','Ludhiana'),
          ('Delhi','Delhi'),
          ('Chandigarh','Chandigarh'),
          ("Chandigarh","Chandigarh"),
          ("Tripura","Tripura")]


class Resumeform(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preferred Job Location',choices=job_city,widget= forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['id','name','dob','gender','locality','city','pin','state','mobile','email',
                    'job_city','profile_image','my_file']
        labels = {'name': 'Full Name', 'dob': 'Date of birth', 'pin': 'pincode',
                'mobile':'Mobile Number','profile_image':'Profile Image','myfile':'Document',
                'email':'Email ID'}
        widgets={
            'name':forms.TextInput(attrs={'class':'size'}),
            'dob':forms.DateInput(attrs={'class':'size','id':'datepicker'}),
            'pin':forms.NumberInput(attrs={'class':'size'}),
            'locality':forms.TextInput(attrs={'class':'size'}),
            'city':forms.TextInput(attrs={'class':'size'}),
            'state':forms.Select(attrs={'class':'size'}),
            'mobile':forms.NumberInput(attrs={'class':'size'}),
            'email':forms.EmailInput(attrs={'class':'size'}),


        }