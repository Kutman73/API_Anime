from django.contrib import admin
from django.conf.urls.static import static
from api_anime import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('anime.api.urls')),
    path('api/v2/', include('anime.api.urls_v2'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
