# Generated by Django 5.1.7 on 2025-03-12 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='id',
            field=models.CharField(editable=False, max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_id',
            field=models.CharField(editable=False, max_length=15, primary_key=True, serialize=False),
        ),
    ]
