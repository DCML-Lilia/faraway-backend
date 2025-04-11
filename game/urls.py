from django.urls import path, include
from .views import PhotoUploadView

urlpatterns = [
    path('upload/', PhotoUploadView.as_view()),  # <- nécessaire pour Flutter
]