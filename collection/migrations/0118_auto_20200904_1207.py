# Generated by Django 2.0.8 on 2020-09-04 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0117_simulation_result_is_new_parameter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation_model',
            name='correct_values',
        ),
        migrations.RemoveField(
            model_name='simulation_model',
            name='errors',
        ),
        migrations.RemoveField(
            model_name='simulation_model',
            name='simulation_data',
        ),
        migrations.RemoveField(
            model_name='simulation_model',
            name='triggered_rules',
        ),
    ]