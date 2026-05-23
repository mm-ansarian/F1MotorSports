from django.urls import path, include
from django.contrib import admin
from news.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('superuser/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('news/', include('news.urls')),
    path('articles/', include('articles.urls')),
]
