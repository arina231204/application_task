from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', ApplicationListView.as_view(), name='apl_list'),
    path('create/', ApplicationCreateView.as_view(), name='apl_create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)