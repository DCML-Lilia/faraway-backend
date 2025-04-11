from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from game.model_loader import model_sanctu, model_region
import os
import shutil
import re

import programme_fond  # Ton script principal

class PhotoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        # Récupère dynamiquement les champs names[0], names[1], etc.
        # Extraire et trier les noms par index


        # On filtre uniquement les champs du type names[0], names[1], etc.
        name_items = [
            (key, value)
            for key, value in request.data.items()
            if re.match(r'names\[\d+\]', key)
        ]

        # Tri par index
        player_names = [
            value for key, value in sorted(
                name_items,
                key=lambda item: int(re.findall(r'names\[(\d+)\]', item[0])[0])
            )
        ]


        print("📥 Requête POST reçue")
        print("🖼️ Fichiers reçus :", request.FILES.getlist('images'))
        print("📊 Count - images:", len(request.FILES.getlist('images')))
        print("✅ Noms ordonnés :", player_names)
        print("📊 Count - names:", len(player_names))


        if not images or not player_names or len(images) != len(player_names):
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        try:

            print("🔍 model_sanctu =", os.path.abspath(model_sanctu))
            print("📂 Fichier existe ?", os.path.exists(model_sanctu))


            # 🔁 Nettoyer le dossier si déjà existant
            base_dir = "dossier_partie"
            if os.path.exists(base_dir):
                shutil.rmtree(base_dir)
            os.makedirs(base_dir)

            # 📸 Enregistrer les photos dans /dossier_partie/J1/photo.jpg, etc.
            for i, img in enumerate(images):
                player_folder = os.path.join(base_dir, f"J{i+1}")
                os.makedirs(player_folder, exist_ok=True)
                # 🔁 Normaliser le nom de fichier en .jpg
                filename = "photo.jpg"
                photo_path = os.path.join(player_folder, filename)

                with open(photo_path, 'wb+') as f:
                    for chunk in img.chunks():
                        f.write(chunk)

                print(f"✅ Image enregistrée : {photo_path}")


            # 📂 Chemin absolu vers le dossier
            chemin = os.path.abspath(base_dir)

            # 🧠 Appel de ta fonction principale
            res = programme_fond.resultat(
                chemin,
                model_sanctu,
                None,  # plus besoin de bdd_sanctu
                model_region,
                None   # plus besoin de bdd_region
            )

            # 📤 Traitement du résultat
            classement_indices = res[0]  # ex: [2, 0, 1]
            scores = res[1]              # ex: [[...], [...], [...]]

            gagnants = [player_names[i] for i in classement_indices]

            return Response({
                "gagnants": gagnants,
                "scores": scores
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
