# Generated by Django 2.0.8 on 2019-02-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0015_uploaded_dataset_list_of_matches'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation_model',
            name='meta_data_facts',
            field=models.TextField(null=True),
        ),
    ]
