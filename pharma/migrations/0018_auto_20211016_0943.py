# Generated by Django 3.2.4 on 2021-10-16 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0017_auto_20171111_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='c_id',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='p_id',
        ),
    ]
