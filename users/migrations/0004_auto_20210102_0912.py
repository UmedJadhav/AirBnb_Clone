# Generated by Django 2.2.5 on 2021-01-02 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210101_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('inr', 'INR')], default='usd', max_length=3),
        ),
    ]
