# Generated by Django 4.1 on 2022-08-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=30)),
                ('Product_price', models.FloatField()),
                ('Product_description', models.CharField(max_length=50)),
                ('inventory', models.IntegerField(default=0)),
            ],
        ),
    ]
