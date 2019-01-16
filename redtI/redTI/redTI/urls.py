from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('users.urls')),
    path('', include('subs.urls')),
] 
if settings.DEBUG:#colocamos esse if, pois usamos essa pasta em tempo de dev, pois quando a gente terminar o proj, devemos usar um servidor pago apenas para a media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
