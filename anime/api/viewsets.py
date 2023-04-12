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
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .validate_serializers import (
    AnimeCreateSerializer,
    AnimeUpdateSerializer,
    SeasonCreateSerializer,
    SeasonUpdateSerializer,
    EpisodeCreateSerializer,
    EpisodeUpdateSerializer,
    MovieCreateSerializer,
    MovieUpdateSerializer,
    ReviewValidateSerializer,
)


class AnimeModelViewSet(ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        serializer = AnimeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data.get('author')
        title = serializer.validated_data.get('title')
        slug = serializer.validated_data.get('slug')
        cover = serializer.validated_data.get('cover')
        description = serializer.validated_data.get('description')
        status_anime = serializer.validated_data.get('status')
        release_date = serializer.validated_data.get('release_date')
        new_anime = Anime.objects.create(author_id=author,
                                         title=title,
                                         slug=slug,
                                         cover=cover,
                                         description=description,
                                         status_id=status_anime,
                                         release_date=release_date)
        new_anime.producer.set(serializer.validated_data.get('producer'))
        new_anime.genre.set(serializer.validated_data.get('genre'))
        new_anime.theme.set(serializer.validated_data.get('theme'))
        new_anime.save()
        return Response(data={'message': 'Data received!',
                              'anime': AnimeSerializers(new_anime).data},
                        status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        anime = self.get_object()
        serializer = AnimeUpdateSerializer(
            data=request.data, context={'id': anime.id}
        )
        serializer.is_valid(raise_exception=True)
        anime.author_id = serializer.validated_data.get('author')
        anime.title = serializer.validated_data.get('title')
        anime.slug = serializer.validated_data.get('slug')
        anime.cover = serializer.validated_data.get('cover')
        anime.description = serializer.validated_data.get('description')
        anime.producer.set(serializer.validated_data.get('producer'))
        anime.genre.set(serializer.validated_data.get('genre'))
        anime.theme.set(serializer.validated_data.get('theme'))
        anime.status_id = serializer.validated_data.get('status')
        anime.release_date = serializer.validated_data.get('release_date')
        anime.save()
        return Response(data={'message': 'Data received!',
                              'anime': AnimeSerializers(anime).data},
                        status=status.HTTP_201_CREATED)


class SeasonModelViewSet(ModelViewSet):
    queryset = AnimeSeason.objects.all()
    serializer_class = SeasonSerializers
    lookup_field = 'pk'

    @action(detail=False, methods=['get'])
    def list_v1(self, request, **kwargs):
        season = self.queryset.filter(
            anime__slug=kwargs['slug']
        )
        serializer = self.serializer_class(season, many=True)
        return Response(data=serializer.data)

    def create(self, request, **kwargs):
        serializer = SeasonCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data.get('author')
        anime = serializer.validated_data.get('anime')
        season_number = serializer.validated_data.get('season_number')
        title = serializer.validated_data.get('title')
        release_date = serializer.validated_data.get('release_date')
        new_season = AnimeSeason.objects.create(
            author_id=author,
            anime_id=anime,
            season_number=season_number,
            title=title,
            release_date=release_date
        )
        new_season.voice_acting.set(
            serializer.validated_data.get('voice_acting')
        )
        new_season.producer.set(serializer.validated_data.get('producer'))
        new_season.save()
        return Response(data={'message': 'Data received!',
                              'anime': SeasonSerializers(new_season).data},
                        status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        season = self.get_object()
        serializer = SeasonUpdateSerializer(
            data=request.data, context={'id': season.id}
        )
        serializer.is_valid(raise_exception=True)
        season.author_id = serializer.validated_data.get('author')
        season.anime_id = serializer.validated_data.get('anime')
        season.season_number = serializer.validated_data.get('season_number')
        season.voice_acting.set(serializer.validated_data.get('voice_acting'))
        season.producer.set(serializer.validated_data.get('producer'))
        season.title = serializer.validated_data.get('title')
        season.release_date = serializer.validated_data.get('release_date')
        season.save()
        return Response(data={'message': 'Data received!',
                              'anime': SeasonSerializers(season).data},
                        status=status.HTTP_201_CREATED)


class EpisodeModelViewSet(ModelViewSet):
    queryset = AnimeEpisode.objects.all()
    serializer_class = EpisodeSerializers
    lookup_field = 'id'

    @action(detail=False, methods=['get'])
    def list_v1(self, request, **kwargs):
        episode = self.queryset.filter(
            season_id=kwargs['pk']
        )
        serializer = self.serializer_class(episode, many=True)
        return Response(data=serializer.data)

    def create(self, request, **kwargs):
        serializer = EpisodeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data.get('author')
        title = serializer.validated_data.get('title')
        season = serializer.validated_data.get('season')
        video = serializer.validated_data.get('video')
        duration = serializer.validated_data.get('duration')
        voice_acting = serializer.validated_data.get('voice_acting')
        episode_number = serializer.validated_data.get('episode_number')
        new_episode = AnimeEpisode.objects.create(
            author_id=author,
            title=title,
            season_id=season,
            video=video,
            duration=duration,
            voice_acting_id=voice_acting,
            episode_number=episode_number,
        )
        new_episode.save()
        return Response(data={'message': 'Data received!',
                              'episode': EpisodeSerializers(new_episode).data},
                        status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        episode = self.get_object()
        serializer = EpisodeUpdateSerializer(
            data=request.data, context={'id': episode.id}
        )
        serializer.is_valid(raise_exception=True)
        episode.author_id = serializer.validated_data.get('author')
        episode.title = serializer.validated_data.get('title')
        episode.season_id = serializer.validated_data.get('season')
        episode.video = serializer.validated_data.get('video')
        episode.voice_acting_id = \
            serializer.validated_data.get('voice_acting')
        episode.episode_number = \
            serializer.validated_data.get('episode_number')
        episode.save()
        return Response(data={'message': 'Data received!',
                              'episode': EpisodeSerializers(episode).data},
                        status=status.HTTP_201_CREATED)


class MovieModelViewSet(ModelViewSet):
    queryset = AnimeMovie.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'pk'

    @action(detail=False, methods=['get'])
    def list_v1(self, request, **kwargs):
        movie = self.queryset.filter(
            anime__slug=kwargs['slug']
        )
        serializer = self.serializer_class(movie, many=True)
        return Response(data=serializer.data)

    def create(self, request, **kwargs):
        serializer = MovieCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data.get('author')
        title = serializer.validated_data.get('title')
        voice_acting = serializer.validated_data.get('voice_acting')
        anime = serializer.validated_data.get('anime')
        duration = serializer.validated_data.get('duration')
        video = serializer.validated_data.get('video')
        new_movie = AnimeMovie.objects.create(
            author_id=author,
            title=title,
            voice_acting_id=voice_acting,
            anime_id=anime,
            duration=duration,
            video=video,
        )
        new_movie.producer.set(serializer.validated_data.get('producer'))
        new_movie.save()
        return Response(data={'message': 'Data received!',
                              'anime_movie': MovieSerializers(new_movie).data},
                        status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        movie = self.get_object()
        serializer = MovieUpdateSerializer(
            data=request.data, context={'id': movie.id}
        )
        serializer.is_valid(raise_exception=True)
        movie.author_id = serializer.validated_data.get('author')
        movie.title = serializer.validated_data.get('title')
        movie.voice_acting = serializer.validated_data.get('voice_acting')
        movie.anime_id = serializer.validated_data.get('anime')
        movie.video = serializer.validated_data.get('video')
        movie.duration = serializer.validated_data.get('duration')
        movie.producer.set(serializer.validated_data.get('producer'))
        movie.movie_number = serializer.validated_data.get('movie_number')
        movie.save()
        return Response(data={'message': 'Data received!',
                              'anime': MovieSerializers(movie).data},
                        status=status.HTTP_201_CREATED)


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializers
    lookup_field = 'pk'

    @action(detail=False, methods=['get'])
    def list_v1(self, request, **kwargs):
        anime_review = self.queryset.filter(
            anime__slug=kwargs['slug']
        )
        serializer = ReviewsSerializers(anime_review, many=True)
        return Response(data=serializer.data)

    def create(self, request, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data.get('author')
        comment = serializer.validated_data.get('comment')
        rating = serializer.validated_data.get('rating')
        anime = serializer.validated_data.get('anime')
        new_review = Review.objects.create(
            author_id=author,
            comment=comment,
            rating=rating,
            anime_id=anime
        )
        new_review.save()
        return Response(data={'message': 'Data received!',
                              'review': ReviewsSerializers(new_review).data},
                        status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        review = self.get_object()
        serializer = ReviewValidateSerializer(
            data=request.data, context={'id': review.id}
        )
        serializer.is_valid(raise_exception=True)
        review.author_id = serializer.validated_data.get('author')
        review.comment = serializer.validated_data.get('comment')
        review.rating = serializer.validated_data.get('rating')
        review.anime_id = serializer.validated_data.get('anime')
        review.save()
        return Response(data={'message': 'Data received!',
                              'review': ReviewsSerializers(review).data},
                        status=status.HTTP_201_CREATED)
