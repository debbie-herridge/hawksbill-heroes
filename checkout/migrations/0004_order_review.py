# Generated by Django 3.2.21 on 2024-03-09 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0007_alter_review_rating'),
        ('checkout', '0003_auto_20240106_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchandise.review'),
        ),
    ]