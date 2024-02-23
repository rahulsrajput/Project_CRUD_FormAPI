from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'home.html')


def create(request):
    form = EmployeeForm()
    context = {'form':form}
    return render(request, 'create.html',context)