from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Weapon(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.CharField(max_length=255, verbose_name='Цена')
    damage = models.CharField(max_length=200, verbose_name='Урон')
    type_of_damage = models.CharField(max_length=200, verbose_name='Тип урона')
    other_properties = models.TextField(blank=True, verbose_name='Различные свойства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = "Оружие"


class Hero(models.Model):
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    hero_img = models.CharField(blank=True, null=True, default="", max_length=255)
    name = models.CharField(max_length=200, blank=True)
    heroes_class = models.CharField(max_length=200, blank=True)
    background = models.CharField(max_length=200, blank=True)
    race = models.CharField(max_length=200, blank=True)
    alignment = models.CharField(max_length=200, blank=True)
    exp_points = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    inspiration = models.BooleanField(default=False)
    proficiency_bonus = models.IntegerField(blank=True, null=True)
    armor_class = models.CharField(max_length=10, blank=True)
    initiative = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    hit_points = models.IntegerField(blank=True, null=True)
    max_hit_points = models.IntegerField(blank=True, null=True)
    temporary_hit_points = models.IntegerField(blank=True, null=True)
    hit_dice = models.CharField(blank=True, null=True, default="", max_length=20)
    death_saves_successes = models.IntegerField(blank=True, null=True)
    death_saves_failures = models.IntegerField(blank=True, null=True)
    other_profs_and_languages = models.TextField(blank=True)
    passive_wisdom = models.IntegerField(blank=True, null=True)
    weapons = models.ManyToManyField(Weapon, blank=True)
    attacks_and_spellcasting = models.TextField(blank=True)
    equipment = models.TextField(blank=True)
    features_and_traits = models.TextField(blank=True)
    # Modification
    strength = models.IntegerField(blank=True, null=True)
    dexterity = models.IntegerField(blank=True, null=True)
    constitution = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    wisdom = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    # Saving throws
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
    # Skills
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
    # Characters views
    personality_traits = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)
    # Money
    gold_coins = models.IntegerField(blank=True, null=True)
    silver_coins = models.IntegerField(blank=True, null=True)
    copper_coins = models.IntegerField(blank=True, null=True)
    electron_coins = models.IntegerField(blank=True, null=True)
    platinum_coins = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.hero_img and hasattr(self.hero_img, 'url'):
            return self.hero_img.url

    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = "Герои"
