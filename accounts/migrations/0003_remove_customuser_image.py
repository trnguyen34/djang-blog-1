# Generated by Django 4.0.10 on 2023-04-17 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
    ]
