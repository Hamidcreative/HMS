# Generated by Django 2.1.7 on 2019-03-12 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_hospital_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='description',
            new_name='name',
        ),
    ]
