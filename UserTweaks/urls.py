from django.contrib import admin
from django.urls import path
from users.views import index, session_end_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('end-session/', session_end_check)
]
