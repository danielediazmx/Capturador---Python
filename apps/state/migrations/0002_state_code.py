# Generated by Django 2.0.5 on 2018-05-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
