# Generated by Django 4.2.1 on 2023-05-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_response_delete_apimodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='contectNumber',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='response',
            name='email',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
