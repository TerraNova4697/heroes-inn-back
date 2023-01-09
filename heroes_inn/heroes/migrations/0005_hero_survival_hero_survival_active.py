# Generated by Django 4.1.3 on 2022-12-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0004_alter_hero_options_alter_weapon_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='survival',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='survival_active',
            field=models.BooleanField(default=False),
        ),
    ]