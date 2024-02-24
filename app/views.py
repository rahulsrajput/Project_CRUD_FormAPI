from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    employee_objects = Employee.objects.all()
    # print(employee_objects)

    context = {'objects':employee_objects}

    return render(request, 'home.html',context)


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

            messages.success(request, 'Successfully Created')
            return HttpResponseRedirect('/')
    else:
        form = EmployeeForm()
    
    context = {'form':form}
    return render(request, 'create.html',context)


def update(request, id):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        # print(form)
        if form.is_valid():
            FirstName = form.cleaned_data['first_name']
            LastName = form.cleaned_data['last_name']
            Email = form.cleaned_data['email']
            Salary = form.cleaned_data['salary']
            Date = form.cleaned_data['date']

            object = Employee(pk=id, first_name=FirstName, last_name=LastName, email=Email, salary=Salary, date_of_joining=Date)

            object.save()
            messages.success(request, 'Successfully Updated')
            return HttpResponseRedirect('/')

    object = Employee.objects.get(pk=id)
    return render(request, 'update.html', context={'object':object})


def delete(request, id):
    object = Employee.objects.get(pk = id)
    print(object)
    object.delete()
    messages.success(request, 'Successfully Deleted')
    return HttpResponseRedirect('/')