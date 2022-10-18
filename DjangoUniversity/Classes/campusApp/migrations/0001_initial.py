# Generated by Django 4.1.2 on 2022-10-18 22:50

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusName', models.CharField(blank=True, default='', max_length=60)),
                ('stateName', models.CharField(blank=True, default='', max_length=2)),
                ('campusID', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'University Campus',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
