# Generated by Django 3.0.8 on 2020-08-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_images_login_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='person_relation_with_name',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
