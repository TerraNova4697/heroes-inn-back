# Generated by Django 4.1.3 on 2022-11-28 09:51

import django.core.validators
from django.db import migrations, models
import heroes.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='acrobatics',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='alignment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hero',
            name='anim_handling',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='arcana',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='armor_class',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='hero',
            name='athletics',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='attacks_and_spellcasting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='background',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hero',
            name='bonds',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='charisma',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.level_or_modif_is_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='charisma_sb',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='constitution',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.level_or_modif_is_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='constitution_sb',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='copper_coins',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='death_saves_failures',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.death_saves_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='death_saves_successes',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.death_saves_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='deception',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='dexterity',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.level_or_modif_is_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='dexterity_sb',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='electron_coins',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='equipment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='exp_points',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='features_and_traits',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='flaws',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='gold_coins',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='heroes_class',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hero',
            name='history',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='hit_dice',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='hit_points',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='ideals',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='initiative',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='insight',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='intelligence',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.level_or_modif_is_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='intelligence_sb',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='intimidation',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='investigation',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='level',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(20, 'Уровень не может быть выше 20'), django.core.validators.MinValueValidator(1, 'Уровень не может быть ниже 1')]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='max_hit_points',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='medicine',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hero',
            name='nature',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='other_profs_and_languages',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='passive_wisdom',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='perception',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='performance',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='personality_traits',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='persuasion',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='platinum_coins',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='proficiency_bonus',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='race',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hero',
            name='religion',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='silver_coins',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='sleight_of_hand',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='speed',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='stealth',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='strength',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.level_or_modif_is_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='strength_sb',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='temporary_hit_points',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='hero',
            name='weapons',
            field=models.ManyToManyField(blank=True, to='heroes.weapon'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='wisdom',
            field=models.IntegerField(blank=True, validators=[heroes.model_validators.level_or_modif_is_valid]),
        ),
        migrations.AlterField(
            model_name='hero',
            name='wisdom_sb',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='other_properties',
            field=models.TextField(blank=True),
        ),
    ]
