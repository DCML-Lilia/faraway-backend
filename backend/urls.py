from django.urls import path, include

urlpatterns = [
    path('api/', include('game.urls')),  # ça ajoute tous les endpoints du fichier game/urls.py sous /api/
]
