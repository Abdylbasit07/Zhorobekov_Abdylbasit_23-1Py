# Generated by Django 4.1.5 on 2023-01-03 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Rate',
            new_name='review_rate',
        ),
    ]
