# Generated by Django 2.2.2 on 2019-06-27 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190622_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_address',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
