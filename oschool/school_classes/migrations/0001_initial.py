# Generated by Django 2.1.8 on 2019-07-17 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=5)),
                ('course_year', models.IntegerField()),
                ('slug', models.SlugField(max_length=5, unique=True)),
            ],
            options={
                'verbose_name': 'lesson',
                'verbose_name_plural': 'lessons',
            },
        ),
    ]
