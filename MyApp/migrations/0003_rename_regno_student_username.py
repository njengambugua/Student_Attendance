# Generated by Django 4.2.7 on 2023-11-27 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_student_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='regno',
            new_name='username',
        ),
    ]