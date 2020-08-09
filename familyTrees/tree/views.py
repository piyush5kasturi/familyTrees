from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import images
from .form import ImageForm
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
        # student_class = request.POST.get('student_class')
        print('person_image', image_person_name)
        person_image = request.FILES['person_image']
        fs = FileSystemStorage()
        print(person_image, image_person_name)
        image_person_name = request.POST.get('image_person_name')
        # student_class = request.POST.get('student_class')
        Databaseee = images(image_person_name=image_person_name, person_image=person_image)
        Databaseee.save()
        return redirect('/tree')
    return render(request , 'tree/form.html')


