# Generated by Django 2.2 on 2020-10-16 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text_important',
            field=models.CharField(default='null', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(max_length=800),
        ),
    ]
