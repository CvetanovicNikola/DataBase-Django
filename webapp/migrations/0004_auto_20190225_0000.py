# Generated by Django 2.1.3 on 2019-02-24 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190224_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='image',
            new_name='photo',
        ),
    ]
