# Generated by Django 3.2.16 on 2023-03-17 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0006_auto_20230317_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article/'),
        ),
    ]
