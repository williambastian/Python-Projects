# Generated by Django 2.2.5 on 2022-11-03 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardGameTracker', '0003_auto_20221103_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgames',
            name='Have_We_Played',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=20),
        ),
    ]
