# Generated by Django 2.2 on 2019-07-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harrastuspassi', '0002_extend_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]