from django.shortcuts import render, HttpResponse
from .models import Teacher, CustomUser, Subject, Course, Enrollment
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def HelloWorld(request):
    return HttpResponse("hello world")

def Registration(request):
    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']
        name = request.POST['nameInput']
        surname = request.POST['surNameInput']
        
        
        user = CustomUser(username = username, password = password, name = name, surname = surname)
        user.save()

        messages.success(request, "Registered new user")

        return redirect("login")
    
    return render(request, "registration.html")

def Login(request):
    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']
        
        
        
        student = CustomUser.objects.get(username=username, password=password)
            
        request.session['name'] = student.Name
        request.session['surname'] = student.Surname
        return redirect("studentBio")
          

    return render(request, "login.html")

# shows student info and <ul> of links to subjects.html, teachers.html, MyCourses.html
def StudentBio(request):
    name = request.session['name']
    surname = request.session['surname']
    

    return render(request, "studentBio.html", {"name": name, "surname":surname})

# shows html page with ALL subjects list(math, pe, chemistry, english)
def Subjects(request):
    object_list = Subject.objects.all()
    return render(request, "subjects.html", {'object_list': object_list})


# shows all courses that student enrolled
def MyCourses(request):
    return None

# student cilcks on Subject and it show all Courses related to subject => cards with title and so on...
def AllCourses(request):
    object_list = Course.objects.all()
    return render(request, "allCoursesList.html", {'object_list': object_list})

# details of the course, user clicks on card in AllCourses and open html page with single course
def Course(request):
    return None

# teacher info panel, see I Teach => teachCourses.html
def TeacherBio(request):
    name = request.session['name']
    surname = request.session['surname']
    

    return render(request, "teacherBio.html", {"name": name, "surname":surname})

# user sees all teachers and their bio
def Teachers(request):
    object_list = Teacher.objects.all()
    return render(request, "teachers.html", {'object_list': object_list})


#single teacher, and shows courses cards he teaches => Course.html
def Teacher(request):
    return None

# shows all course that teachers teaches => course.html
def TeachCourses(request):
    # join by teacher
    # coursesTeacherTeaches = Course.objects.filter(Teacher = currentTeacher)
    
    return None
