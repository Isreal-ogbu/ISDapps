# Generated by Django 4.1 on 2022-08-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
