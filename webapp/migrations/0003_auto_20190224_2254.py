# Generated by Django 2.1.3 on 2019-02-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_employee_ocupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to='emp_picture'),
        ),
        migrations.AddField(
            model_name='employee',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='firstname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lastname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ocupation',
            field=models.CharField(max_length=20),
        ),
    ]
