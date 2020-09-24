# Generated by Django 3.1 on 2020-09-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('author_surname', models.CharField(max_length=50)),
                ('author_nationality', models.CharField(max_length=50)),
                ('author_description', models.CharField(max_length=400)),
            ],
        ),
    ]
