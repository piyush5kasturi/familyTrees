from django.db import models

# Create your models here.
class images(models.Model):
    images_id = models.AutoField
    image_person_name=models.TextField()
    person_image=models.ImageField(upload_to="tree\images", default="")

    def __str__(self):
        return self.image_person_name

