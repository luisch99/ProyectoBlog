# Generated by Django 4.0.6 on 2022-08-04 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=models.TextField(max_length=400),
        ),
    ]