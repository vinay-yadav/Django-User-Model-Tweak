from django.contrib import admin
from django.urls import path, include
from users.views import index, session_end_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls'))
]
