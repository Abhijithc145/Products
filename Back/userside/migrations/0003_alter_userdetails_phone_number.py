# Generated by Django 4.1 on 2022-08-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0002_alter_userdetails_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
