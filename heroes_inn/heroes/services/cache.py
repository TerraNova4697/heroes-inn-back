import os
import redis
import json

from abc import ABC, abstractmethod
from .singleton_meta import SingletonMeta
from heroes.models import (
    Weapon, Spell, Item, Feature,
)
from heroes.serializers import (
    WeaponSerializer, SpellSerializer, ItemSerializer, FeatureSerializer,
)


class CacheSource(ABC):

    @abstractmethod
    def connection(self):
        pass

    @abstractmethod
    def get_item(self, namespace, id):
        pass

    @abstractmethod
    def set_item(self, namespace, id, item):
        pass

    @abstractmethod
    def get_items(self, namespace):
        pass

    @abstractmethod
    def set_items(self, namespace, items):
        pass


class RedisCache(CacheSource):
    __metaclass__ = SingletonMeta
    _REDIS_PORT = os.getenv('REDIS_PORT')
    _REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
    _REDIS_HOST = os.getenv('REDIS_HOST')

    def __init__(self):
        self.pool = redis.ConnectionPool(host=self._REDIS_HOST,
                                         port=self._REDIS_PORT,
                                         password=self._REDIS_PASSWORD,
                                         db=1)

    @property
    def connection(self):
        if not hasattr(self, '_connection'):
            self.getConnection()
        return self._connection

    def getConnection(self):
        self._connection = redis.Redis(connection_pool=self.pool)

    def get_item(self, name, key):
        data = self.connection.hget(name, key)
        if data:
            return json.loads(data)
        return None

    def set_item(self, name, item):
        item_id = item['id']
        return self.connection.hset(name, item_id, json.dumps(item))

    def get_items(self, name):
        pass

    def prepopulate(self):
        spells = SpellSerializer(Spell.objects.all(), many=True).data
        self.connection.hmset('spells', spells)

        weapon = WeaponSerializer(Weapon.objects.all(), many=True).data
        self.connection.hmset('weapon', weapon)

        items = ItemSerializer(Item.objects.all(), many=True).data
        self.connection.hmset('items', items)

        features = FeatureSerializer(Feature.objects.all(), many=True).data
        self.connection.hmset('features', features)

    def set_items(self, namespace, items):
        pass


class Cache:

    def __init__(self, cache_source):
        self.cache_source = cache_source

    def get_item(self, name, key):
        return self.cache_source.get_item(name, key)

    def set_item(self, name, item):
        return self.cache_source.set_item(name, item)

    def get_items(self, name):
        return self.cache_source.get_items(name)

    def set_items(self, key, items):
        self.cache_source.set_items(key, items)

    def prepopulate_cache(self):
        self.cache_source.prepopulate()
