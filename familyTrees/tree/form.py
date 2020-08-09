from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model=images
        fields=['image_person_name' , 'person_image']