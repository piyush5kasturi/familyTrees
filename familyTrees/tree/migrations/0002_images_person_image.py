# Generated by Django 3.0.8 on 2020-07-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='person_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]