# Generated by Django 2.0.8 on 2020-01-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0082_uploaded_dataset_object_id_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation_model',
            name='sorted_attribute_ids',
            field=models.TextField(default='[]'),
            preserve_default=False,
        ),
    ]
