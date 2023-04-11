from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AnimeModelViewSet,
    SeasonModelViewSet,
    EpisodeModelViewSet,
    MovieModelViewSet,
    ReviewModelViewSet
)

router = DefaultRouter()
router.register(r'anime', AnimeModelViewSet)
router.register(r'season', SeasonModelViewSet)
router.register(r'episode', EpisodeModelViewSet)
router.register(r'movie', MovieModelViewSet)
router.register(r'review', ReviewModelViewSet)


urlpatterns = [
    path('', include(router.urls))
]
