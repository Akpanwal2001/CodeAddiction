# Generated by Django 3.2.5 on 2021-07-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210715_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='char',
            field=models.IntegerField(default=200),
        ),
    ]
