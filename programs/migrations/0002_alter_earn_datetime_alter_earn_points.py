# Generated by Django 4.0.5 on 2022-06-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earn',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='earn',
            name='points',
            field=models.IntegerField(),
        ),
    ]
