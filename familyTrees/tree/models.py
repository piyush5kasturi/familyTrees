from django.db import models


# relation=(
#     ('father','FATHER'),
#     ('mother','MOTHER'),
#     ('cousin','COUSIN'),
#     ('sibling','SIBLING'),
# )

# Create your models here.
class images(models.Model):
    images_id = models.AutoField
    image_person_name=models.TextField()
    person_image=models.ImageField(upload_to="tree\images", default="")
    person_relation=models.CharField(max_length=20)
    person_relation_with_name = models.CharField(max_length=20, default="" ,blank=True,null=True)
    login_username=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.image_person_name

