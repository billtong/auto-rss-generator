from django.contrib import admin
from django.urls import path

import server.view as view

urlpatterns = [
    path('rss/slack-channel/', view.get_rss),
    path('admin/', admin.site.urls),
]
