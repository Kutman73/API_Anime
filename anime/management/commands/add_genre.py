from django.core.management import BaseCommand
from anime.models import Genre


class Command(BaseCommand):
    def handle(self, *args, **options):
        genres = (
            'Приключения', 'Боевик', 'Комедия', 'Повседневность',
            'Романтика', 'Драма', 'Фантастика', 'Фэнтези',
            'Мистика', 'Детектив', 'Триллер', 'Психология'
        )
        Genre.objects.all().delete()
        for genre in genres:
            Genre.objects.create(genre_name=genre)
        print("Added genres")
