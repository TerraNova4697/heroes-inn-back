from rest_framework import serializers

from .models import (
    Character,
    Weapon,
    Spell,
    Item,
    Feature,
    ModificationSet,
    SavingThrowsSet,
    CharacterSkills,
    CharacterViewsSet,
    CharacterMoney,
)


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'char_img', 'name', 'heroes_class', 'race', 'level']


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class ModificationSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModificationSet
        fields = '__all__'


class SavingThrowsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingThrowsSet
        fields = '__all__'


class CharacterSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSkills
        fields = '__all__'


class CharacterViewsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterViewsSet
        fields = '__all__'


class CharacterMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterMoney
        fields = '__all__'


class CharacterDetailsSerializer(CharacterSerializer):
    weapons = WeaponSerializer(many=True, required=False)
    attacks_and_spellcasting = SpellSerializer(many=True, required=False)
    equipment = ItemSerializer(many=True, required=False)
    features_and_traits = FeatureSerializer(many=True, required=False)
    modifications_set = ModificationSetSerializer(many=False, required=False)
    saving_throws_set = SavingThrowsSetSerializer(many=False, required=False)
    skills_set = CharacterSkillsSerializer(many=False, required=False)
    char_views = CharacterViewsSetSerializer(many=False, required=False)
    char_money = CharacterMoneySerializer(many=False, required=False)

    class Meta(CharacterSerializer.Meta):
        fields = '__all__'


class CharacterImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to character."""

    class Meta:
        model = Character
        fields = ['id', 'char_img']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
