# Generated by Django 3.2.4 on 2021-08-24 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210824_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='chipmaker',
            name='owned_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.chipmaker'),
        ),
    ]
