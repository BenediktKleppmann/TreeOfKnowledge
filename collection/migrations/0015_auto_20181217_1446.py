# Generated by Django 2.0.8 on 2018-12-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0014_auto_20181217_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded_dataset',
            name='data_source',
            field=models.TextField(default='UN data'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Datasource',
        ),
    ]