# Generated by Django 3.0.8 on 2020-08-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0007_images_person_relation_with_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_username', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
    ]