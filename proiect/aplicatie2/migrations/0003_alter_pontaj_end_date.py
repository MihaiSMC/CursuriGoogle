# Generated by Django 3.2.9 on 2021-12-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie2', '0002_pontaj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontaj',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]
