from django.contrib import admin
from .models import (
    Weapon,
    Hero,
    Spell,
    Item,
    Feature,
)
# Register your models here.

admin.site.register(Weapon)
admin.site.register(Hero)
admin.site.register(Spell)
admin.site.register(Item)
admin.site.register(Feature)
