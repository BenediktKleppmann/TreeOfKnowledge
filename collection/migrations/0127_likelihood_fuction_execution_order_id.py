# Generated by Django 2.0.8 on 2020-09-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0126_simulation_model_manually_set_initial_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='likelihood_fuction',
            name='execution_order_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
