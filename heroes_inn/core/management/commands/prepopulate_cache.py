from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command for loading cache for predefined data."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        pass
        # self.stdout.write('Populating cache with predefined data...')
        # cache = Cache(RedisCache())
        # cache.prepopulate_cache()
        # self.stdout.write(self.style.SUCCESS('Database available!'))
