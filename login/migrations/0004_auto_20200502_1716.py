# Generated by Django 3.0.4 on 2020-05-02 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_autority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='autority',
            new_name='authority',
        ),
    ]