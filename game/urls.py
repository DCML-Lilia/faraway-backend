# game/urls.py

from django.urls import path
from .views import PhotoUploadView  # ou tout autre view que tu veux exposer

urlpatterns = [
    path('upload/', PhotoUploadView.as_view()),  # donc /api/upload/
    path('game/', PhotoUploadView.as_view()),    # donc /api/game/
]
