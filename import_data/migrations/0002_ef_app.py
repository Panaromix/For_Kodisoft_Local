# Generated by Django 2.0.4 on 2018-04-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EF_App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_load', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='file_for_export_apps/')),
            ],
            options={
                'verbose_name': 'Файл для экспорта - Apps',
                'verbose_name_plural': 'Файл для экспорта - Apps',
            },
        ),
    ]