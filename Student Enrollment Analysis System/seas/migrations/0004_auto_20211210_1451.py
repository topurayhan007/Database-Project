# Generated by Django 3.2.9 on 2021-12-10 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seas', '0003_auto_20211210_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_T',
            fields=[
                ('facultyID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('facultyName', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='section_t',
            name='faculty',
            field=models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='seas.faculty_t'),
            preserve_default=False,
        ),
    ]