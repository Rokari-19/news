# Generated by Django 5.1.7 on 2025-03-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_newsitem_dislikes_alter_newsitem_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='content',
            field=models.TextField(max_length=35000),
        ),
    ]
