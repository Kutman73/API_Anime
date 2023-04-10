from django.contrib import admin
from .models import (
    Anime,
    Genre,
    Theme,
    Producer,
    VoiceActing,
    StatusAnime,
    AnimeSeason,
    AnimeEpisode,
    AnimeMovie,
    Review
)

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Theme)
admin.site.register(Producer)
admin.site.register(StatusAnime)
admin.site.register(VoiceActing)
admin.site.register(AnimeSeason)
admin.site.register(AnimeEpisode)
admin.site.register(AnimeMovie)
admin.site.register(Review)
