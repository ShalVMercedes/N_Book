# Generated by Django 4.0.6 on 2022-08-14 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_profile_img_profile_profileimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profileimg',
            new_name='profile_img',
        ),
    ]
