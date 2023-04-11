from django.urls import path
from .viewsets import (
    AnimeModelViewSet,
    SeasonModelViewSet,
    EpisodeModelViewSet,
    MovieModelViewSet,
    ReviewModelViewSet
)


urlpatterns = [
    path('anime/',
         AnimeModelViewSet.as_view({'get': 'list'})),
    path('anime/<slug:slug>/',
         AnimeModelViewSet.as_view({'get': 'retrieve'})),
    path('anime/<slug:slug>/seasons/',
         SeasonModelViewSet.as_view({'get': 'list'})),
    path('anime/<slug:slug>/season-<int:pk>/',
         SeasonModelViewSet.as_view({'get': 'retrieve'})),
    path('anime/<slug:slug>/season-<int:pk>/episodes/',
         EpisodeModelViewSet.as_view({'get': 'list'})),
    path('anime/<slug:slug>/season-<int:pk>/episode-<int:id>/',
         EpisodeModelViewSet.as_view({'get': 'retrieve'})),
    path('anime/<slug:slug>/movies/',
         MovieModelViewSet.as_view({'get': 'list'})),
    path('anime/<slug:slug>/movie-<int:pk>/',
         MovieModelViewSet.as_view({'get': 'retrieve'})),
    path('anime/<slug:slug>/reviews/',
         ReviewModelViewSet.as_view({'get': 'list'})),
    path('anime/<slug:slug>/review-<int:pk>/',
         ReviewModelViewSet.as_view({'get': 'retrieve'})),
]
