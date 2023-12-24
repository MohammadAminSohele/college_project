# Generated by Django 5.0b1 on 2023-12-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_degree_description_remove_major_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('unit', models.IntegerField()),
                ('time_start', models.DateField()),
                ('time_end', models.DateField()),
                ('Instructors', models.ManyToManyField(to='students.instructors')),
                ('Major', models.ManyToManyField(to='students.major')),
            ],
        ),
    ]
