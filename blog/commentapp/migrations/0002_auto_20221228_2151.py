# Generated by Django 3.2.16 on 2022-12-28 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0005_alter_article_content'),
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='articleapp.article'),
        ),
        migrations.CreateModel(
            name='AnonymousComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anonymouscomment', to='articleapp.article')),
            ],
        ),
    ]