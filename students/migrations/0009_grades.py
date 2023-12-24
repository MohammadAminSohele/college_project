# Generated by Django 4.2.7 on 2023-12-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_semesters_course_offerings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('register_date', models.DateField()),
                ('student', models.ManyToManyField(to='students.student')),
            ],
        ),
    ]
