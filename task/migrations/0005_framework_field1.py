# Generated by Django 2.0.1 on 2022-12-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_merge_20220913_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='framework',
            name='field1',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
