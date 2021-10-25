from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.static import static

urlpatterns = [
    path('root/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
