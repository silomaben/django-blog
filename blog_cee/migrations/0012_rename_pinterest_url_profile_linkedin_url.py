# Generated by Django 4.2.3 on 2023-07-15 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_cee', '0011_profile_pinterest_url_profile_facebook_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Pinterest_url',
            new_name='linkedin_url',
        ),
    ]
