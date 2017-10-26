from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from main.views import MainPage
from subscribed_people.views import SubscribeCreate


urlpatterns = [
    url(r'^$', MainPage.as_view()),
    url(r'^', include('articles.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/cards/', include('cards_api.urls')),
    url(r'^subscribe/', SubscribeCreate.as_view(), name='subscribe')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
