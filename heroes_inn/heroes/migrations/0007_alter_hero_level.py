# Generated by Django 4.1.3 on 2023-01-02 05:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0006_alter_hero_hero_img_alter_hero_hit_dice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='level',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(20, 'Уровень не может быть выше 20'), django.core.validators.MinValueValidator(0, 'Уровень не может быть ниже 1')]),
        ),
    ]
