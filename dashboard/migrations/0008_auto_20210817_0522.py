# Generated by Django 2.2 on 2021-08-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210817_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovenconsumption',
            name='date_info',
            field=models.DateTimeField(max_length=100, null=True),
        ),
    ]