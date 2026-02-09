from django.shortcuts import render, redirect
from .models import Student, Attendance
from datetime import date
from .models import AppUser



def home(request):
    return render(request, 'studapp/home.html')


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')

        Student(name=name, roll_number=int(roll)).save()
        return redirect('home')

    return render(request, 'studapp/add_student.html')


def mark_attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        status = request.POST.get('status')

        student = Student.objects.get(id=student_id)

        Attendance(
            student=student,
            date=date.today(),
            is_present=True if status == 'present' else False
        ).save()

        return redirect('home')

    return render(request, 'studapp/mark_attendance.html', {'students': students})


def view_attendance(request):
    records = Attendance.objects.all()
    return render(request, 'studapp/view_attendance.html', {'records': records})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if AppUser.objects(username=username).first():
            return render(request, 'studapp/signup.html', {'error': 'User already exists'})

        AppUser(username=username, password=password).save()
        return redirect('login')

    return render(request, 'studapp/signup.html')

def mongo_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = AppUser.objects(username=username, password=password).first()

        if user:
            request.session['user'] = str(user.id)
            return redirect('home')

        return render(request, 'studapp/login.html', {'error': 'Invalid credentials'})

    return render(request, 'studapp/login.html')

def mongo_logout(request):
    request.session.flush()
    return redirect('login')

def mongo_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

@mongo_login_required
def home(request):
    return render(request, 'studapp/home.html')
                  






# Create your views here.
