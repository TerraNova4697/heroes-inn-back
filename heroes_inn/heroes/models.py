from django.contrib.auth import get_user_model
from django.db import models


class Hero(models.Model):
    pass


class Character(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    char_img = models.CharField(blank=True, null=True, default="", max_length=255)
    name = models.CharField(max_length=200, blank=True)
    heroes_class = models.CharField(max_length=200, blank=True)
    background = models.CharField(max_length=200, blank=True)
    race = models.CharField(max_length=200, blank=True)
    alignment = models.CharField(max_length=200, blank=True)
    exp_points = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    inspiration = models.BooleanField(default=False)
    prof_bonus = models.IntegerField(blank=True, null=True)
    armor_class = models.CharField(max_length=10, blank=True)
    initiative = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    hit_points = models.IntegerField(blank=True, null=True)
    max_hit_points = models.IntegerField(blank=True, null=True)
    temporary_hit_points = models.IntegerField(blank=True, null=True)
    hit_dice = models.CharField(blank=True, null=True, default="", max_length=20)
    death_successes = models.IntegerField(blank=True, null=True)
    death_failures = models.IntegerField(blank=True, null=True)
    other_profs_and_langs = models.TextField(blank=True)
    passive_wisdom = models.IntegerField(blank=True, null=True)
    weapons = models.ManyToManyField('Weapon', blank=True)
    attacks_and_spellcasting = models.ManyToManyField('Spell', blank=True)
    equipment = models.ManyToManyField('Item', blank=True)
    features_and_traits = models.ManyToManyField('Feature', blank=True)
    modifications_set = models.OneToOneField('ModificationSet', null=True, on_delete=models.SET_NULL)
    saving_throws_set = models.OneToOneField('SavingThrowsSet', null=True, on_delete=models.SET_NULL)
    skills_set = models.OneToOneField('CharacterSkills', null=True, on_delete=models.SET_NULL)
    char_views = models.OneToOneField('CharacterViewsSet', null=True, on_delete=models.SET_NULL)
    char_money = models.OneToOneField('CharacterMoney', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.hero_img and hasattr(self.hero_img, 'url'):
            return self.hero_img.url


class Weapon(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name', unique=True)
    weapon_type = models.CharField(max_length=32, verbose_name='Weapon Type', default='Uncategorized')
    rarity = models.CharField(max_length=32, verbose_name='Rarity', default='Uncategorized')
    weight = models.IntegerField(default=-1)
    weapon_category = models.CharField(max_length=32, default='Uncategorized')
    weapon_range = models.CharField(max_length=32, default='0')
    dmg_type = models.CharField(max_length=32, default="Uncategorized")
    dmg1 = models.CharField(max_length=32, default='-1')
    dmg2 = models.CharField(max_length=32, default='-1')
    bonus_weapon = models.CharField(max_length=32, default='-1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Weapon'
        verbose_name_plural = "Weapon"


class Spell(models.Model):
    name = models.CharField(max_length=200, verbose_name='Spell', unique=True)
    level = models.IntegerField(default=-1)
    source = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='Item', unique=True)
    source = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=200, verbose_name='Feature', unique=True)
    source = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ModificationSet(models.Model):
    strength = models.IntegerField(blank=True, null=True)
    dexterity = models.IntegerField(blank=True, null=True)
    constitution = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    wisdom = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Set of character modifications'


class SavingThrowsSet(models.Model):
    strength_sb_active = models.BooleanField(default=False)
    strength_sb = models.IntegerField(blank=True, null=True)
    dexterity_sb_active = models.BooleanField(default=False)
    dexterity_sb = models.IntegerField(blank=True, null=True)
    constitution_sb_active = models.BooleanField(default=False)
    constitution_sb = models.IntegerField(blank=True, null=True)
    intelligence_sb_active = models.BooleanField(default=False)
    intelligence_sb = models.IntegerField(blank=True, null=True)
    wisdom_sb_active = models.BooleanField(default=False)
    wisdom_sb = models.IntegerField(blank=True, null=True)
    charisma_sb_active = models.BooleanField(default=False)
    charisma_sb = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Set of character saving throws'


class CharacterSkills(models.Model):
    acrobatics_active = models.BooleanField(default=False)
    acrobatics = models.IntegerField(blank=True, null=True)
    anim_handling_active = models.BooleanField(default=False)
    anim_handling = models.IntegerField(blank=True, null=True)
    arcana_active = models.BooleanField(default=False)
    arcana = models.IntegerField(blank=True, null=True)
    athletics_active = models.BooleanField(default=False)
    athletics = models.IntegerField(blank=True, null=True)
    deception_active = models.BooleanField(default=False)
    deception = models.IntegerField(blank=True, null=True)
    history_active = models.BooleanField(default=False)
    history = models.IntegerField(blank=True, null=True)
    insight_active = models.BooleanField(default=False)
    insight = models.IntegerField(blank=True, null=True)
    intimidation_active = models.BooleanField(default=False)
    intimidation = models.IntegerField(blank=True, null=True)
    investigation_active = models.BooleanField(default=False)
    investigation = models.IntegerField(blank=True, null=True)
    medicine_active = models.BooleanField(default=False)
    medicine = models.IntegerField(blank=True, null=True)
    nature_active = models.BooleanField(default=False)
    nature = models.IntegerField(blank=True, null=True)
    perception_active = models.BooleanField(default=False)
    perception = models.IntegerField(blank=True, null=True)
    performance_active = models.BooleanField(default=False)
    performance = models.IntegerField(blank=True, null=True)
    persuasion_active = models.BooleanField(default=False)
    persuasion = models.IntegerField(blank=True, null=True)
    religion_active = models.BooleanField(default=False)
    religion = models.IntegerField(blank=True, null=True)
    sleight_of_hand_active = models.BooleanField(default=False)
    sleight_of_hand = models.IntegerField(blank=True, null=True)
    stealth_active = models.BooleanField(default=False)
    stealth = models.IntegerField(blank=True, null=True)
    survival_active = models.BooleanField(default=False)
    survival = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Set of character skills'


class CharacterViewsSet(models.Model):
    personality_traits = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)

    def __str__(self):
        return 'Set of character views'


class CharacterMoney(models.Model):
    gold_coins = models.IntegerField(blank=True, null=True)
    silver_coins = models.IntegerField(blank=True, null=True)
    copper_coins = models.IntegerField(blank=True, null=True)
    electron_coins = models.IntegerField(blank=True, null=True)
    platinum_coins = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f' {self.gold_coins} {self.silver_coins} {self.copper_coins} {self.electron_coins} {self.platinum_coins}'
