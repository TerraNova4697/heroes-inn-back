# Generated by Django 4.1.3 on 2023-07-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_alter_weapon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='weapon_range',
            field=models.CharField(default='0', max_length=32),
        ),
    ]
