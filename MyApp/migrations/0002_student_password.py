# Generated by Django 4.2.7 on 2023-11-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
