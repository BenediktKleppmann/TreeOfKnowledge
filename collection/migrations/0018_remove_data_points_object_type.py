# Generated by Django 2.0.8 on 2019-02-14 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0017_object'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_points',
            name='object_type',
        ),
    ]
