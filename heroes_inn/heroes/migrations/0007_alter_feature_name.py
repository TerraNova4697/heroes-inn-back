# Generated by Django 4.1.3 on 2023-07-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0006_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
