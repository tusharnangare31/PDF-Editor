# Generated by Django 5.0.2 on 2025-03-29 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_tools', '0002_userprofile_is_email_verified_userprofile_otp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='otp_expiry',
        ),
    ]
