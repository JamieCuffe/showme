# Generated by Django 2.0.4 on 2018-04-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_auto_20180423_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='name',
        ),
        migrations.AlterField(
            model_name='students',
            name='certsObtained',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='students',
            name='courseBasket',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='students',
            name='coursesCompleted',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='students',
            name='degree',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='major',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='pinnedCertificates',
            field=models.CharField(max_length=1000000),
        ),
    ]
