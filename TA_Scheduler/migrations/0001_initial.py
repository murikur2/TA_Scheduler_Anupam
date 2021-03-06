# Generated by Django 3.2 on 2021-04-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='myContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=20)),
                ('emailAddress', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='myCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=20)),
                ('courseNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='myCourseInstructors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.IntegerField()),
                ('userName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='myLab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labName', models.CharField(max_length=20)),
                ('labNumber', models.IntegerField()),
            ],
        ),
    ]
