# Generated by Django 3.1.3 on 2020-11-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201108_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
