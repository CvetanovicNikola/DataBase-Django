# Generated by Django 2.1.3 on 2019-02-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20190225_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='static/profile_default.jpg', upload_to='emp_picture/'),
        ),
    ]
