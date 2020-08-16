from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import images
from .form import ImageForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage

# from .models import Post

def index(request):
    data = images.objects.all()
    print(data)
    n = len(data)
    # nslides=n//4+ceil((n/4)-(n//4))
    params = {'no_of_slides': n, 'range': range(1, n), 'database': data}
    return render(request, 'tree/index.html', params)


def form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        image_person_name = request.POST.get('image_person_name')
        person_relation=request.POST.get('select')
        person_relation_with_name = request.POST.get('selects')
        # student_class = request.POST.get('student_class')
        print('person_image', image_person_name)
        person_image = request.FILES['person_image']
        fs = FileSystemStorage()
        print(person_image, image_person_name)
        image_person_name = request.POST.get('image_person_name')
        # student_class = request.POST.get('student_class')
        Databaseee = images(image_person_name=image_person_name, person_image=person_image , person_relation=person_relation, person_relation_with_name=person_relation_with_name)
        Databaseee.save()
        return redirect('/tree')
    data = images.objects.all()
    print(data)
    n = len(data)
    # nslides=n//4+ceil((n/4)-(n//4))
    params = {'no_of_slides': n, 'range': range(1, n), 'database': data}
    return render(request , 'tree/form.html',params)

def signup(request):
    if request.method == 'POST':
         username = request.POST.get('user_username_person')
         user_email=request.POST.get('email')
         user_pass=request.POST.get('password')
         print(username,user_email,user_pass)
         database=User.objects.create_user(username=username,email=user_email,password=user_pass)
         database.save()
         return redirect('/tree/login')

    return render(request,'tree/signup.html')

def login(request):
    if request.method == 'POST':
        username=request.POST.get('Username')
        password=request.POST.get('password')
        data=auth.authenticate(username=username,password=password)
        if data is not None:
            auth.login(request,data)
            return redirect('/tree/index')
        else:
            messages.error(request,'Please enter correct username or password')

    return render(request,'tree/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/tree/logout')

def logouts(request):
    return render(request, 'tree/logout.html')

