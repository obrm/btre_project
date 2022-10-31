# Generated by Django 4.1.1 on 2022-10-24 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_delete_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listings',
            new_name='listing',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]