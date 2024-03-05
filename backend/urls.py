from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views.home import home
from core.views.upload_podcast import upload_podcast
from core.views.list_podcasts import list_podcasts
from core.views.podcast_detail import podcast_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('subir-podcast/', upload_podcast, name="upload_podcast"),
    path('podcasts/', list_podcasts, name="podcasts"),
    path('podcasts/<slug:slug>/', podcast_detail, name="podcast_detail"),
    path('auth/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
