# Generated by Django 4.2.3 on 2024-09-14 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_registrant_delete_event_delete_governingbodymember_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrant',
            old_name='course',
            new_name='event',
        ),
    ]
