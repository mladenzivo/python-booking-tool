# Generated by Django 2.2 on 2022-02-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20220206_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfilesdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]