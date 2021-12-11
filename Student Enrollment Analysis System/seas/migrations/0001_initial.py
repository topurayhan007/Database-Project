# Generated by Django 3.2.9 on 2021-12-11 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom_T',
            fields=[
                ('roomID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('roomCapacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_T',
            fields=[
                ('courseID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=50)),
                ('creditHour', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_T',
            fields=[
                ('facultyID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('facultyName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School_T',
            fields=[
                ('schoolTitle', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionNo', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('noOfEnrolledStudent', models.IntegerField()),
                ('semester', models.CharField(default='N/A', max_length=6)),
                ('year', models.CharField(max_length=4)),
                ('day', models.CharField(max_length=4)),
                ('blocked', models.CharField(max_length=4)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seas.course_t')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seas.faculty_t')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seas.classroom_t')),
            ],
        ),
        migrations.CreateModel(
            name='Department_T',
            fields=[
                ('deptCode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('deptName', models.CharField(max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seas.school_t')),
            ],
        ),
        migrations.AddField(
            model_name='course_t',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seas.department_t'),
        ),
    ]
