from django.http import HttpResponse
from django.shortcuts import render
from .models import images
# from .models import Post

def index(request):
    image=images.objects.all()
    print(image)
    params={'images':image}
    return render(request,'tree/index.html',params)

def form(request):
    return render(request,'tree/form.html')

# if request.method == 'POST':
    #     if request.POST.get('image_person_name') and request.POST.get('person_image'):
    #         image_person_name=request.POST.get('image_person_name')
    #         person_image=request.POST.get('person_image')
    #         .save()
