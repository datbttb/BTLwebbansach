# Generated by Django 4.1.6 on 2023-03-07 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image',
        ),
    ]
