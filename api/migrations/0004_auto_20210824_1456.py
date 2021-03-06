# Generated by Django 3.2.4 on 2021-08-24 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_chipmaker_owned_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpuarchitecture',
            name='developer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='architectures', to='api.chipmaker'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gpu',
            name='architecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpus', to='api.gpuarchitecture'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpus', to='api.chipmaker'),
        ),
        migrations.AlterField(
            model_name='lithography',
            name='fab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='api.fab'),
        ),
    ]
