from django.core.management import BaseCommand
from anime.models import Theme


class Command(BaseCommand):
    def handle(self, *args, **options):
        themes = (
            'Боевые искусства', 'История', 'Меха', 'Полиция',
            'Сенен', 'Ужасы', 'Вампиры', 'Демоны', 'Космос',
            'Музыка', 'Самураи', 'Спорт', 'Школа', 'Военное',
            'Игры', 'Магия', 'Пародия', 'Седзе', 'Суперсила'
        )
        Theme.objects.all().delete()
        for theme in themes:
            Theme.objects.create(theme_name=theme)
        print("Added themes")
