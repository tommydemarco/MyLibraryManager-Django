# Generated by Django 3.1 on 2020-09-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_remove_author_author_age'),
        ('books', '0005_auto_20200903_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
        ),
    ]