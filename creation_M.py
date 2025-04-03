import cv2
import numpy as np
import os
import tensorflow as tf
from PIL import Image, ExifTags

def detect_card_edges(image_path, output_path):
    '''fonction qui permet de détecter les bords des cartes sur une photo de cartes placées en ligne'''
    # Charger l'image
    image = cv2.imread(image_path)
    if image is None:
        print("Erreur : Impossible de charger l'image. Vérifiez le chemin.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour réduire le bruit
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Détection des contours avec Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Trouver les contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Créer une image noire de la même taille que l'originale
    black_background = np.zeros_like(image)

    # Filtrer les contours qui ressemblent à des cartes et les dessiner sur l'image noire
    detected_cards = []
    for cnt in contours:
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        if len(approx) >= 4:  # Vérifier si la forme est assez polygonale
            detected_cards.append(approx)

    # Dessiner les contours détectés en vert sur le fond noir
    cv2.drawContours(black_background, detected_cards, -1, (0, 255, 0), 2)

    # Sauvegarder l'image des contours détectés
    cv2.imwrite(output_path, black_background)
    print(f"Image des contours enregistrée sous : {output_path}")

    # Afficher l'image résultante avec les contours verts
    #cv2.imshow("Contours Detected", black_background)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


def detect_green_rectangles(image_path, chemin_photo_a_decouper, folder_name, numero, output_dir):
    '''fonction qui permet d'enregistrer un fichier par carte dans un dossier dont le nom est entré par l'utilisateur dans les arguments de la fonction'''
    # Définir le dossier de sortie spécifié par l'utilisateur
    output_folder = os.path.join(output_dir, folder_name) #il faudrait plutôt spécifier le chemin d'accès au dossier dans lequel on veut enregistrer les splits

    # Charger l'image originale pour la découpe
    original_image = cv2.imread(image_path)
    image = original_image.copy()

    # Vérifier si l'image est bien chargée
    if image is None:
        print(f"Erreur : Impossible de charger l'image {image_path}. Vérifiez le chemin et le fichier.")
        return

    # Convertir l'image en espace de couleur HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Définir la plage de couleur verte en HSV
    lower_green = np.array([40, 40, 40])                                        # Limite inférieure
    upper_green = np.array([80, 255, 255])                                      # Limite supérieure

    # Créer un masque pour la couleur verte
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Trouver les contours des objets détectés
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Obtenir la taille de l'image
    image_height, image_width, _ = image.shape
    min_area = (image_height * image_width) / 50                                # Aire minimale requise

    rectangles = []

    # Détection des rectangles
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:  # Vérifier si l'aire dépasse 1/15 de l'image
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            if len(approx) >= 4:  # Vérifier si c'est un quadrilatère
                x, y, w, h = cv2.boundingRect(approx)
                rectangles.append((x, y, w, h))

    # Trier les rectangles selon leur position horizontale
    rectangles.sort()

    split_positions = []

    # Identifier les positions de découpe
    for i in range(len(rectangles) - 1):
        x1, y1, w1, h1 = rectangles[i]
        x2, y2, w2, h2 = rectangles[i + 1]
        middle_x = (x1 + w1 + x2) // 2                                          # Position entre les deux rectangles
        split_positions.append(middle_x)

    # Créer un dossier de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    original_image = cv2.imread(chemin_photo_a_decouper)
    # Sauvegarder les images découpées depuis l'image originale
    def split_image(original_image, split_positions):
        previous_x = 0
        for i, x in enumerate(split_positions + [image_width]):
            if previous_x < x:  # Vérifier qu'on ne découpe pas une zone vide
                cropped_image = original_image[:, previous_x:x]
                output_path = os.path.join(output_folder, f'split_{numero-i}.png')
                cv2.imwrite(output_path, cropped_image)
                print(f"Image enregistrée : {output_path}")
            previous_x = x

    split_image(original_image, split_positions)

    # Afficher l'image résultante
    #cv2.imshow('Detected Rectangles', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

###decoupage des photos


def decouper_ligne_photo(chemin_photo_a_decouper, folder_name, numero, chemin_joueur):
    ''''''

    chemin_fichier_intermédiaire=chemin_joueur+"/contours.png"
    #détection des bords des cartes
    detect_card_edges(chemin_photo_a_decouper,chemin_fichier_intermédiaire)
    #découpage de la photo ligne
    detect_green_rectangles(chemin_fichier_intermédiaire,chemin_photo_a_decouper, folder_name,numero,chemin_joueur)



def extract_frames(image_path, output_folder):
    '''fonction qui extrait les 3 cadres de la photo prise par l'utilisateur en respectant l'orientation portrait.'''
    try:
        # Créer le dossier de sortie s'il n'existe pas
        os.makedirs(output_folder, exist_ok=True)

        # Ouvrir l'image et corriger l'orientation EXIF si nécessaire
        img = Image.open(image_path)
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = img._getexif()
            if exif and orientation in exif:
                if exif[orientation] == 3:
                    img = img.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    img = img.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    img = img.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            # Pas d'EXIF ou orientation déjà correcte
            pass

        img_width, img_height = img.size

        # Calculer les dimensions des cadres selon le ratio 4.3
        frame_width = img_width
        frame_height = int(frame_width / 4.3)

        # Calculer les espacements et le point de départ
        total_height = 3 * frame_height + 2 * 10
        top_offset = (img_height - total_height) // 2

        for i in range(3):
            top = top_offset + i * (frame_height + 10)
            box = (0, top, frame_width, top + frame_height)
            frame = img.crop(box)
            frame.save(f"{output_folder}/frame{i}.png")

        print("Extraction des cadres réussie en format portrait !")
    except Exception as e:
        print(f"Erreur lors de l'extraction des cadres : {e}")





def decouper_photo_joueur(chemin_joueur):
    '''fonction qui va extraire les 3 lignes de cartes sur chaque photo dans 3 fichiers différents, puis extraire un fichier par carte, dont les noms sont rangés dans l'ordre de comptage des points des cartes'''
    #découper en lignes
    extract_frames(chemin_joueur+"/photo.jpg",chemin_joueur)
    #on procède ensuite au découpage de chaque ligne
    decouper_ligne_photo(chemin_joueur+"/frame0.png","sanctuaires",0,chemin_joueur)                             #on s'occupe d'abord de la première ligne, c'est-à-dire des sanctuaires
    decouper_ligne_photo(chemin_joueur+"/frame2.png","regions____",3,chemin_joueur)                             #on s'occupe ensuite de la dernière ligne (c'est celle sur laquelle la
                                                                                #première carte dont il faut compter les points est située)
    decouper_ligne_photo(chemin_joueur+"/frame1.png","regions____",7,chemin_joueur)                             #on s'occupe ensuite de la première ligne de cartes régions

##
#                            |                                                    |
#                            |     Génération des listes S et R grâce à l'IA      |
#                            |____________________________________________________|




# 📏 Paramètres
IMG_SIZE = 128  # Même taille que celle utilisée lors de l'entraînement



# 📸 Fonction pour tester une image sanctuaire
def predict_sanctu(image_path,model_sanctu,bdd_sanctu):
    model=tf.keras.models.load_model(model_sanctu)
    # 📂 Labels (mappage des indices de classes aux noms des cartes)
    labels_dict = {i: f"sanctuaire{i+1}" for i in range(45)}


    # Charger l'image
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Erreur : Impossible de charger l'image '{image_path}'")
        return

    # Prétraitement : redimensionnement et normalisation
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0                                                           # Normalisation des pixels entre 0 et 1
    img = np.expand_dims(img, axis=0)                                           # Ajouter une dimension batch

    # 🔍 Prédiction
    prediction = model.predict(img)
    pred_class = np.argmax(prediction)                                          # Trouver la classe avec la plus forte probabilité
    confidence = np.max(prediction)                                             # Confiance de la prédiction

    # 📌 Affichage du résultat
    print(f"🔎 Carte reconnue : {labels_dict[pred_class]} (Confiance : {confidence:.2f})")
    return int(labels_dict[pred_class][10:])



# 📸 Fonction pour tester une image région
def predict_region(image_path,model_region,bdd_region):
    model=tf.keras.models.load_model(model_region)
    # 📂 Labels (mappage des indices de classes aux noms des cartes)
    labels_dict = {i: f"region{i+1}" for i in range(68)}



    # Charger l'image
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Erreur : Impossible de charger l'image '{image_path}'")
        return

    # Prétraitement : redimensionnement et normalisation
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0                                                           # Normalisation des pixels entre 0 et 1
    img = np.expand_dims(img, axis=0)                                           # Ajouter une dimension batch

    # 🔍 Prédiction
    prediction = model.predict(img)
    pred_class = np.argmax(prediction)                                          # Trouver la classe avec la plus forte probabilité
    confidence = np.max(prediction)                                             # Confiance de la prédiction

    # 📌 Affichage du résultat
    print(f"🔎 Carte reconnue : {labels_dict[pred_class]} (Confiance : {confidence:.2f})")
    return int(labels_dict[pred_class][6:])

# Génération de la liste S

def generer_S(chemin_dossier_joueur,model_sanctu,bdd_sanctu):
    nb_sanctu=len(os.listdir(chemin_dossier_joueur+"/sanctuaires"))             #nombre de sanctuaires du joueur concerné
    S=[]                                                                        #initialisation de la liste S
    for i in range(0,nb_sanctu):                                                  #pour chaque carte sanctuaire, on identifie à quel sanctuaire cela correspond
        S.append(predict_sanctu(chemin_dossier_joueur+"/sanctuaires/split_"+str(int(-i))+".png",model_sanctu,bdd_sanctu)) #on ajoute le numéro du sanctuaire détécté à S
    return S

#Génération de la liste R

def generer_R(chemin_dossier_joueur,model_region,bdd_region):
    nb_regions=8                                                                #nombre de régions
    R=[]                                                                        #initialisation de la liste R
    for i in range(nb_regions):                                                 #pour chaque carte région, on identifie à quel région cela correspond
        R.append(predict_region(chemin_dossier_joueur+f"/regions____/split_{i}.png",model_region,bdd_region)) #on ajoute le numéro du sanctuaire détécté à R
    return R


##
#                            |                                                    |
#                            |              Génération de la liste M              |
#                            |____________________________________________________|


def liste_M(chemin_dossier_partie,model_sanctu,bdd_sanctu,model_region,bdd_region):
    '''Cette fonction génère la liste M qui contient toutes les données nécessaires au calcul des points de la partie.
    On présuppose que les dossiers dossier_partie et dossier_joueur sont déjà créés et que chaque dossier_joueur contient la photo des cartes jouées correspondante à ce joueur. On présuppose donc que les dossiers avant le traitement de cette fonction sont de la forme :
        |--dossier_partie
            |
            |--J1
                |--photo.jpg
            |
            |--J2
                |--photo.jpg
            .
            .
    La fonction, après exécution, aura organisé les dossiers de cette manière :
        |--dossier_partie
            |
            |--J1
                |
                |--sanctuaires
                    |--split_-1.png
                    |--split_-2.png
                    .
                    .
                    .
                |--regions____
                    |--split_0.png
                    |--split_1.png
                    .
                    .
                    .
            |
            |--J2
                |
                .
                .
            .
            .
    '''
    #découpage des photos et organisation dans les dossiers
    nb_joueur=len(os.listdir(chemin_dossier_partie))
    M=[]                                                                        #initialisation de la liste à renvoyer à la fin
    for i in range(nb_joueur):
        decouper_photo_joueur(chemin_dossier_partie+f"/J{i+1}")
        S=generer_S(chemin_dossier_partie+f"/J{i+1}",model_sanctu,bdd_sanctu)
        R=generer_R(chemin_dossier_partie+f"/J{i+1}",model_region,bdd_region)
        M.append([S,R])
    return M


