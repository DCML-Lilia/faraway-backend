from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# ✅ Fonction simple qui retourne "ok" à la racine
def home(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('', home),                          # ✅ Ajoute une réponse à la racine "/"
    path('api/', include('game.urls')),      # Tes endpoints sont ici
    path('admin/', admin.site.urls),         # (optionnel si tu veux admin)
]
