# Generated by Django 3.1.2 on 2020-10-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60)),
                ('CourseNum', models.IntegerField()),
                ('InstructorName', models.CharField(max_length=60)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]
