# Generated by Django 4.2.5 on 2023-09-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestorantApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='RestorantApp/static/images'),
        ),
    ]
