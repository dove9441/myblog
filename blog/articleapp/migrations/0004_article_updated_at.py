# Generated by Django 3.2.16 on 2022-12-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0003_alter_article_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
