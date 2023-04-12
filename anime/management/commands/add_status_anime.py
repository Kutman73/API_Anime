from django.core.management import BaseCommand
from anime.models import StatusAnime


class Command(BaseCommand):
    def handle(self, *args, **options):
        StatusAnime.objects.all().delete()
        StatusAnime.objects.create(status='Вышел')
        StatusAnime.objects.create(status='Онгоинг')
        StatusAnime.objects.create(status='Анонс')
        print("Added statuses")
