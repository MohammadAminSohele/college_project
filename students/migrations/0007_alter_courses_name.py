# Generated by Django 5.0b1 on 2023-12-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
