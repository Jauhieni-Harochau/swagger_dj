# Generated by Django 3.2.4 on 2021-08-24 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210824_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='chipmaker',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.image'),
        ),
    ]
