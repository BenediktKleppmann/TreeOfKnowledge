# Generated by Django 2.0.8 on 2020-09-15 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0124_remove_simulation_model_nb_of_parameters_to_keep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation_model',
            name='validation_data',
        ),
    ]
