# Generated by Django 3.0.5 on 2020-05-30 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
    ]