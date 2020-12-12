# Generated by Django 2.2 on 2020-09-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=40)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
