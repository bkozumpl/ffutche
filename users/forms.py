from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(max_length=45)
    password2 = forms.CharField(max_length=45)
    firstname = forms.CharField(max_length=45)
    middlename = forms.CharField(max_length=45)
    lastname = forms.CharField(max_length=45)
    gender = forms.CharField(max_length=45)
    type_of_user = forms.CharField(max_length=45)
    phone1 = forms.IntegerField()
    phone2 = forms.IntegerField()
    address1 = forms.CharField(max_length=45)
    address2 = forms.CharField(max_length=45)
    dob_day = forms.CharField(max_length=45)
    dob_month = forms.CharField(max_length=45)
    dob_year = forms.CharField(max_length=45)
    cityofbirth = forms.CharField(max_length=45)
    countryofbirth = forms.CharField(max_length=45)
    marital_status = forms.CharField(max_length=45)
    number_of_children = forms.CharField(max_length=45)
    occupation = forms.CharField(max_length=45)
    employer_name = forms.CharField(max_length=45)
    employer_address = forms.CharField(max_length=45)


    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'firstname','middlename','lastname',
                  'gender','type_of_user', 'phone1', 'phone2', 'address1', 'address2', 'dob_day', 'dob_month',
                  'dob_year','cityofbirth', 'countryofbirth', 'marital_status', 'number_of_children', 'occupation',
                  'employer_name', 'employer_address']

