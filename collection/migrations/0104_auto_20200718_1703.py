# Generated by Django 2.0.8 on 2020-07-18 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0103_simulation_model_aborted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulation_model',
            old_name='max_df_size',
            new_name='max_number_of_instances',
        ),
    ]
