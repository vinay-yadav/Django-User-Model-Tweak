from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetails.as_view())
]
