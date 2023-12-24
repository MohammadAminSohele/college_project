# Generated by Django 4.2.7 on 2023-12-22 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0018_alter_course_offerings_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_Offering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.courses')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.instructors')),
            ],
        ),
    ]
