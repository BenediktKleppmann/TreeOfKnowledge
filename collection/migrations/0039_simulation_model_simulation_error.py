# Generated by Django 2.0.8 on 2019-04-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0038_simulation_model_linegraph_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation_model',
            name='simulation_error',
            field=models.FloatField(null=True),
        ),
    ]
