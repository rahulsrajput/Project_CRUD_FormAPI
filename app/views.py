from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')


def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            salary = form.cleaned_data['salary']
            date = form.cleaned_data['date']

            E = Employee(first_name=first_name, last_name=last_name,email=email,salary=salary,date_of_joining=date)
            E.save()

            return HttpResponseRedirect('/')
    else:
        form = EmployeeForm()
    
    context = {'form':form}
    return render(request, 'create.html',context)


def update(request):
    return render(request, 'update.html')


def delete(request):
    pass