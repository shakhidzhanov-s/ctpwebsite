# Generated by Django 2.0.5 on 2018-08-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0022_auto_20180811_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='mission')),
            ],
        ),
        migrations.RemoveField(
            model_name='institute',
            name='mission',
        ),
    ]