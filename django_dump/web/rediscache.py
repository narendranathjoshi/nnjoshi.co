import redis
import pickle
from django.utils import timezone

from django.conf import settings


class RedisCache:
    def __init__(self, conn, prefix=''):
        self.conn = conn
        self.prefix = prefix

    def get_key(self, key):
        return "%s_%s" % (self.prefix, key)

    def get(self, key):
        return self.conn.get(self.get_key(key))

    def set(self, key, value, expires):
        return self.conn.set(self.get_key(key), value, expires)

    def pickled_get(self, key):
        cached = self.get(key)
        if cached:
            return pickle.loads(cached)

    def pickled_set(self, key, value, expires):
        value = pickle.dumps(value)
        return self.set(key, value, expires)

    def delete(self, key):
        return self.conn.delete(self.get_key(key))

    def set_timestamp(self, key):
        return self.pickled_set("dtime_%s" % key,
                                timezone.now(), 60 * 60 * 24 * 7)

    def get_timestamp(self, key):
        return self.pickled_get("dtime_%s" % key)


connection = redis.StrictRedis(**settings.REDIS_CACHE)

resume_cache = RedisCache(connection, prefix='res')
