import server.view as view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('rss/', view.get_rss),
    path('admin/', admin.site.urls),
]
