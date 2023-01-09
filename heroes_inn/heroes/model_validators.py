from django.core.exceptions import ValidationError


def level_or_modif_is_valid(value):
    if 0 <= value <= 20:
        return value
    else:
        raise ValidationError("Уровень может быть только в диапозоне от 1 до 20")


def death_saves_valid(value):
    if 0 <= value <= 3:
        return value
    else:
        raise ValidationError("Не может быть меньше 0 или больше 3")
