from django.contrib import admin
from django.conf.urls.static import static
from api_anime.settings import base
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('anime.api.urls')),
    path('api/v2/', include('anime.api.urls_v2'))
]

urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

if base.DEBUG:
    urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
