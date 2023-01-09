from rest_framework import serializers

from .models import Hero, Weapon


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'hero_img', 'name', 'heroes_class', 'race', 'level']


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    # weapons = WeaponSerializer(many=True)

    def validate_level(self, value):
        if not 1 <= value <= 20:
            raise serializers.ValidationError("Уровень должен быть в диапазоне от 1 до 20")
        return value

    def validate_strength(self, value):
        if value < 0 or value > 20:
            raise serializers.ValidationError("Сила не может быть меньше 0 или больше 20")
        return value

    def validate_dexterity(self, value):
        if value < 0 or value > 20:
            raise serializers.ValidationError("Ловкость не может быть меньше 0 или больше 20")
        return value

    def validate_constitution(self, value):
        if value < 0 or value > 20:
            raise serializers.ValidationError("Телосложение не может быть меньше 0 или больше 20")
        return value

    def validate_intelligence(self, value):
        if value < 0 or value > 20:
            raise serializers.ValidationError("Интеллект не может быть меньше 0 или больше 20")
        return value

    def validate_wisdom(self, value):
        if value < 0 or value > 20:
            raise serializers.ValidationError("Мудрость не может быть меньше 0 или больше 20")
        return value

    def validate_charisma(self, value):
        if value < 0 or value > 20:
            raise serializers.ValidationError("Харизма не может быть меньше 0 или больше 20")
        return value

    def validate_death_saves_successes(self, value):
        if not 0 <= value <= 3:
            raise serializers.ValidationError("Кличество успешных спасбросков от смерти должно быть в диапазоне от 0 до 3")
        return value

    def validate_death_saves_failures(self, value):
        if not 0 <= value <= 3:
            raise serializers.ValidationError("Кличество проваленных спасбросков от смерти должно быть в диапазоне от 0 до 3")
        return value

    class Meta:
        model = Hero
        fields = '__all__'


class HeroWeaponSerializer(serializers.ModelSerializer):
    weapons = WeaponSerializer(many=True)

    class Meta:
        model = Hero
        fields = '__all__'


