import sys
sys.path.append(r"c:\users\lilia\desktop\dcml\faraway\programmation")

import creation_M as creation
import calcul_points as calcul

def resultat(chemin_dossier_partie,model_sanctu,bdd_sanctu,model_region,bdd_region):
    #traitement images
    M=creation.liste_M(chemin_dossier_partie,model_sanctu,bdd_sanctu,model_region,bdd_region)
    #traitement calcul
    res=calcul.partie(M)
    print(res)
    return res


