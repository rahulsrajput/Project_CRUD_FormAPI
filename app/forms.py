from django import forms

class EmployeeForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    salary = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    date = forms.DateField(input_formats=['%Y-%m-%d'],widget=forms.SelectDateWidget(attrs={'class':'form-control'}))