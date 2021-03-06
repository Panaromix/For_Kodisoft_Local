# Generated by Django 2.0.4 on 2018-04-14 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0006_auto_20180414_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='eb_order',
            name='order_id_unic',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='eb_order',
            name='revenue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eb_order',
            name='session_key',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='import_data.EB_Session'),
        ),
        migrations.AddField(
            model_name='eb_order',
            name='time_create',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
