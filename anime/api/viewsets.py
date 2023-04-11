from rest_framework.viewsets import ModelViewSet
from anime.models import (
    Anime,
    AnimeSeason,
    AnimeEpisode,
    AnimeMovie,
    Review,
)
from .serializers import (
    AnimeSerializers,
    SeasonSerializers,
    EpisodeSerializers,
    MovieSerializers,
    ReviewsSerializers,
)


class AnimeModelViewSet(ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers
    lookup_field = 'slug'


class SeasonModelViewSet(ModelViewSet):
    queryset = AnimeSeason.objects.all()
    serializer_class = SeasonSerializers
    lookup_field = 'id'


class EpisodeModelViewSet(ModelViewSet):
    queryset = AnimeEpisode.objects.all()
    serializer_class = EpisodeSerializers
    lookup_field = 'id'


class MovieModelViewSet(ModelViewSet):
    queryset = AnimeMovie.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'id'


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializers
    lookup_field = 'id'

