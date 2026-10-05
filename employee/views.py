from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.
def home(request):
    return render(request, "employee/home.html")

def login(request):
    if request.method == 'POST':
        emp_id = request.POST.get('empid', '').strip()
        user_pass = request.POST.get('password', '').strip()
        if not emp_id or not user_pass:
            messages.error(request, "Please enter both Employee ID and Password!")
            return render(request, 'employee/login.html')

        try:
            emp = employee.objects.get(empid=int(emp_id), password=user_pass)

            request.session['empid'] = emp.empid
            return redirect('employee') 

        except (employee.DoesNotExist, ValueError):
            messages.error(request, "Incorrect Employee ID or Password!")

    return render(request, 'employee/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        city = request.POST.get('city', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        

        if name and password and email and age and city:
            emp = employee.objects.create(name=name, age=age, city=city, email=email, password=password)
            emp.save()
            messages.success(request, f"Registration Successful! Your Employee ID is: {emp.empid}")
            return redirect('login')
    return render(request, "employee/register.html")

def emp(request):
    return render(request, "employee/employee.html")

def update(request):
    if 'empid' not in request.session:
        messages.error(request, "Please login first!")
        return redirect('login')

    session_empid = request.session['empid']
    try:
        emp = employee.objects.get(empid=session_empid)
    except employee.DoesNotExist:
        messages.error(request, "Employee record not found!")
        request.session.flush()
        return redirect('login')


    if request.method == 'POST':
        new_name = request.POST.get('name', '').strip()
        new_age = request.POST.get('age', '').strip()
        new_city = request.POST.get('city','').strip()
        new_email = request.POST.get('email', '').strip()
        new_password = request.POST.get('password', '').strip()

        emp.name = new_name 
        emp.age = new_age
        emp.city = new_city
        emp.password = new_password
        emp.email = new_email
        emp.save() 

        messages.success(request, "Profile updated successfully!")
        return redirect('update')

    return render(request, 'employee/update.html', {'emp': emp})


def delete(request):
    if 'empid' not in request.session:
        messages.error(request, "Please login first!")
        return redirect('login')
    
    try:
        emp = employee.objects.get(empid=request.session['empid'])
    except employee.DoesNotExist:
        messages.error(request, "Employee not found!")
        request.session.flush()
        return redirect('login')
    
    if request.method == 'POST':
        emp.delete()
        request.session.flush()
        
        messages.success(request, "Your account has been deleted successfully!")
        return redirect('home')

    return render(request, "employee/delete.html", {'emp': emp})


def display(request):
    employees = employee.objects.all()
    return render(request, "employee/display.html", {'employees': employees})

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully!")
    return redirect('login')