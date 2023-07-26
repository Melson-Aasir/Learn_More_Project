from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from StudentApp.models import City, Course, Student, Trainer


def login_fun(request):
    if request.method == 'POST':
        u_name = request.POST['txtname']
        u_pwd = request.POST['txtpwd']
        user = authenticate(username=u_name, password=u_pwd)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                request.session['Name'] = u_name
                return redirect('home')
        else:
            return render(request, 'login.html', {'msg': 'Enter proper username and password'})
    else:
        return render(request, 'login.html', {'msg': ''})


def register(request):
    if request.method == 'POST':
        u_name = request.POST['txtname']
        u_email = request.POST['txtemail']
        u_password = request.POST['txtpwd']

        u2 = User.objects.filter(Q(username=u_name)).exists()
        u3 = User.objects.filter(Q(email=u_email)).exists()

        # print(u2)
        if u2 or u3:
            return render(request, 'register.html', {'msg': 'username and email already exists'})
        else:
            u1 = User.objects.create_superuser(username=u_name, password=u_password, email=u_email)

            u1.save()
            return redirect('log')
    else:
        return render(request, 'register.html', {'msg': ''})


@never_cache
def logout_fun(request):
    logout(request)
    return redirect('log')


@login_required
@never_cache
def course_fun(request):
    return render(request, 'course.html')


@login_required
@never_cache
def home_fun(request):
    return render(request, 'home.html', {'data': request.session['Name']})


# student

@login_required
@never_cache
def insert(request):
    if request.method == 'POST':
        s1 = Student()
        s1.stud_name = request.POST['txtsname']
        s1.stud_phno = request.POST['txtsphno']
        s1.stud_email = request.POST['txtsemail']
        s1.stud_fees = request.POST['txtfees']
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlcourse'])  # if foreign key we've to use this method to fecth data
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.save()
        return redirect('insert')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, 'student.html', {'CourseData': course, 'CityData': city})


@login_required
@never_cache
def display(request):
    data = Student.objects.all()
    return render(request, 'display_student.html', {'data': data})


@login_required
@never_cache
def update(request, id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.stud_name = request.POST['txtsname']
        s1.stud_phno = request.POST['txtsphno']
        s1.stud_email = request.POST['txtsemail']
        s1.stud_fees = request.POST['txtfees']
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlcourse'])  # if foreign key we've to use this method to fecth data
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.save()
        return redirect('display')
    else:
        return render(request, 'update_student.html', {'data': s1, 'citydata': city, 'coursedata': course})


@login_required
@never_cache
def delete(request, id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


# Trainer

@login_required
@never_cache
def insert_trainer(request):
    if request.method == 'POST':
        t1 = Trainer()
        t1.trainer_name = request.POST['txttname']
        t1.trainer_phno = request.POST['txttphno']
        t1.trainer_email = request.POST['txttemail']
        t1.trainer_salary = request.POST['txtsalary']
        t1.teaching_course = Course.objects.get(course_name=request.POST['ddlcourse'])        # if foreign key we've to use this method to fecth data
        t1.trainer_city = City.objects.get(city_name=request.POST['ddlcity'])
        t1.save()
        return redirect('insert_trainer')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, 'insert_trainer.html', {'CourseData': course, 'CityData': city})


@login_required
@never_cache
def display_trainer(request):
    data = Trainer.objects.all()
    return render(request, 'display_trainer.html', {'data': data})


@login_required
@never_cache
def update_trainer(request, id):
    t1 = Trainer.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        t1.trainer_name = request.POST['txttname']
        t1.trainer_phno = request.POST['txttphno']
        t1.trainer_email = request.POST['txttemail']
        t1.trainer_salary = request.POST['txtsalary']
        t1.teaching_course = Course.objects.get(course_name=request.POST['ddlcourse'])  # if foreign key we've to use this method to fecth data
        t1.trainer_city = City.objects.get(city_name=request.POST['ddlcity'])
        t1.save()
        return redirect('display_trainer')
    else:
        return render(request, 'update_trainer.html', {'data': t1, 'citydata': city, 'coursedata': course})


@login_required
@never_cache
def delete_trainer(request, id):
    t1 = Trainer.objects.get(id=id)
    t1.delete()
    return redirect('display_trainer')
