# Generated by Django 3.0.6 on 2020-06-04 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_appi', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='topi',
            new_name='topic',
        ),
    ]
