# Generated by Django 3.2.5 on 2021-07-29 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewslettersUser',
            new_name='NewsletterUser',
        ),
    ]
