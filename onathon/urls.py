
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from board import views as board_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler404 = board_views.page_not_found
handler500 = board_views.internal_error