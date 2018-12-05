# Generated by Django 2.0.8 on 2018-11-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='newsletter_subscriber',
            name='email_hash',
            field=models.CharField(default='111111', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsletter_subscriber',
            name='is_alchemist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsletter_subscriber',
            name='is_archivist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsletter_subscriber',
            name='is_templar',
            field=models.BooleanField(default=False),
        ),
    ]