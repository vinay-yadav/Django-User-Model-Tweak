from django import urls
from django.contrib import admin
from django.urls import path, include
from users.views import index, session_end_check
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('', include('polls.urls')),
    path('books/', include('library.urls')),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs')
]
