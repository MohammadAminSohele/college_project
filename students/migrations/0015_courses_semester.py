# Generated by Django 4.2.7 on 2023-12-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_grades_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.semesters'),
        ),
    ]
