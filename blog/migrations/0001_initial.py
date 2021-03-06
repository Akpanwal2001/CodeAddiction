# Generated by Django 3.2.5 on 2021-07-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=120)),
                ('thumbnail', models.ImageField(blank=True, upload_to='images/')),
                ('datetime', models.DateTimeField(blank=True)),
            ],
        ),
    ]
