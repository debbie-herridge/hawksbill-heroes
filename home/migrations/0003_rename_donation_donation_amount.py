# Generated by Django 3.2.21 on 2024-03-07 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240307_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='donation',
            new_name='amount',
        ),
    ]