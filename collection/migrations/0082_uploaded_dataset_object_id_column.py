# Generated by Django 2.0.8 on 2020-01-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0081_auto_20200108_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaded_dataset',
            name='object_id_column',
            field=models.TextField(default='[1,2,3,4,5,6,7,8,9,10]'),
            preserve_default=False,
        ),
    ]