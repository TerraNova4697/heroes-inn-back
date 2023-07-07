# import json
# import os

# from django.db import transaction
# from django.conf import settings
# from django.http import HttpResponse

# from heroes.models import (
#     Weapon,
#     Spell,
#     Item,
#     Feature,
# )


# @transaction.atomic
# def home_view(request):
#     """Prepopulate DB."""

#     """Prepopulate with Weapons and Items."""
#     file_path = os.path.join(settings.BASE_DIR, 'resources', 'resources', 'items', 'items.json')
#     with open(file_path) as f:
#         data = json.load(f)
#         for item in data['item']:
#             if 'weaponCategory' in item:
#                 w = Weapon.objects.create(
#                     name=item['name'],
#                     rarity=item['rarity'],
#                     weapon_category=item['weaponCategory'],
#                     dmg_type=item['dmgType'],
#                     dmg1=item['dmg1'],
#                 )
#                 if 'range' in item:
#                     w.weapon_range = item['range']
#                 if 'dmg2' in item:
#                     w.dmg2 = item['dmg2']
#                 if 'bonusWeapon' in item:
#                     w.bonus_weapon = item['bonusWeapon']
#                 if 'weight' in item:
#                     w.weight = item['weight']
#                 w.save()
#             else:
#                 if not Item.objects.filter(name=item['name']).exists():
#                     Item.objects.create(
#                         name=item['name']
#                     )

#     """Prepopulate with Spells."""
#     directory_path = os.path.join(settings.BASE_DIR, 'resources', 'resources', 'spells')
#     files_list = os.listdir(directory_path)
#     for json_file in files_list:
#         file_path = os.path.join(directory_path, json_file)
#         if os.path.getsize(file_path) != 0:
#             with open(file_path) as f:
#                 data = json.load(f)
#                 for spell in data['spell']:
#                     Spell.objects.create(
#                         name=spell['name'],
#                         level=spell['level']
#                     )

#     """Prepopulate with Features."""
#     file_path = os.path.join(settings.BASE_DIR, 'resources', 'resources', 'feats', 'feats.json')
#     with open(file_path) as f:
#         data = json.load(f)
#         for feat in data['feat']:
#             if not Feature.objects.filter(name=feat['name']).exists():
#                 Feature.objects.create(
#                     name=feat['name']
#                 )

#     file_path = os.path.join(settings.BASE_DIR, 'resources', 'resources', 'other_features', 'other_features.json')
#     with open(file_path) as f:
#         data = json.load(f)
#         for feat in data['optionalfeature']:
#             if not Feature.objects.filter(name=feat['name']).exists():
#                 Feature.objects.create(
#                     name=feat['name']
#                 )

#     return HttpResponse('This view is for preloading DB only.')
