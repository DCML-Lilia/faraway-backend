regions={
    1  : (1,1,0,1,0,0),
    2  : (2,0,0,1,0,3),
    3  : (0,0,0,1,0,1),
    4  : (1,0,1,1,0,0),
    5  : (0,1,0,1,0,1),
    6  : (1,0,0,1,1,3),
    7  : (0,1,1,1,0,0),
    8  : (0,1,0,1,1,1),
    9  : (0,0,0,1,0,3),
    10 : (0,0,0,1,0,0),
    11 : (0,0,0,1,0,1),
    12 : (0,0,1,1,1,2),
    13 : (0,0,0,1,0,3),
    14 : (0,0,1,1,0,0),
    15 : (0,0,0,1,1,1),
    16 : (0,1,0,1,0,0),
    17 : (1,0,0,1,0,3),
    18 : (0,1,0,1,0,1),
    19 : (0,0,1,1,0,0),
    20 : (0,0,0,0,1,1),
    21 : (0,0,0,0,0,3),
    22 : (0,0,0,0,1,1),
    23 : (1,1,0,0,0,0),
    24 : (1,0,0,0,0,3),
    25 : (0,0,0,0,0,2),
    26 : (0,1,0,0,0,0),
    27 : (0,0,0,0,0,2),
    28 : (1,0,0,0,0,0),
    29 : (0,0,1,0,0,2),
    30 : (1,0,0,0,0,0),
    31 : (0,0,0,0,0,2),
    32 : (1,1,0,0,0,0),
    33 : (0,0,0,0,1,2),
    34 : (0,1,0,0,0,1),
    35 : (0,1,0,0,0,2),
    36 : (0,0,0,0,0,0),
    37 : (0,0,0,0,0,2),
    38 : (1,0,0,0,0,1),
    39 : (1,0,1,0,0,0),
    40 : (0,0,0,0,0,3),
    41 : (0,0,1,1,0,1),
    42 : (0,0,0,1,0,2),
    43 : (1,0,0,1,0,3),
    44 : (0,0,0,1,0,2),
    45 : (1,0,0,1,0,1),
    46 : (0,0,0,1,1,3),
    47 : (0,0,0,1,0,2),
    48 : (0,1,0,1,0,0),
    49 : (0,0,0,1,1,3),
    50 : (1,0,0,1,0,2),
    51 : (1,0,0,1,0,3),
    52 : (0,0,0,1,0,0),
    53 : (0,1,0,1,0,2),
    54 : (0,1,0,1,0,1),
    55 : (1,0,0,1,1,3),
    56 : (0,0,1,1,0,2),
    57 : (0,0,0,1,0,0),
    58 : (0,0,0,1,1,1),
    59 : (0,0,0,1,1,2),
    60 : (0,0,0,1,1,3),
    61 : (0,0,1,1,0,1),
    62 : (0,0,0,1,1,2),
    63 : (0,0,0,1,1,1),
    64 : (0,0,0,1,1,3),
    65 : (0,0,0,1,1,2),
    66 : (0,0,0,1,0,3),
    67 : (0,0,0,1,1,1),
    68 : (0,0,0,1,0,3)

}


sanctuaires={
    1  : (-1,1,-1),
    2  : (-1,-1,-1),
    3  : (0,0,-1),
    4  : (0,-1,-1),
    5  : (2,1,-1),
    6  : (2,0,-1),
    7  : (-1,-1,-1),
    8  : (1,1,-1),
    9  : (0,-1,-1),
    10 : (1,0,-1),
    11 : (0,1,-1),
    12 : (1,-1,-1),
    13 : (2,-1,-1),
    14 : (1,-1,-1),
    15 : (-1,-1,-1),
    16 : (-1,1,-1),
    17 : (-1,-1,-1),
    18 : (-1,-1,-1),
    19 : (-1,-1,-1),
    20 : (-1,-1,-1),
    21 : (-1,-1,-1),
    22 : (-1,-1,-1),
    23 : (-1,-1,-1),
    24 : (-1,-1,2),
    25 : (-1,-1,2),
    26 : (0,-1,2),
    27 : (-1,1,2),
    28 : (-1,-1,2),
    29 : (2,-1,0),
    30 : (0,-1,0),
    31 : (-1,-1,0),
    32 : (-1,0,0),
    33 : (1,-1,0),
    34 : (-1,1,1),
    35 : (0,-1,1),
    36 : (-1,-1,1),
    37 : (1,-1,1),
    38 : (-1,-1,1),
    39 : (1,-1,3),
    40 : (0,-1,3),
    41 : (-1,-1,3),
    42 : (2,-1,3),
    43 : (-1,1,3),
    44 : (0,-1,-1),
    45 : (-1,-1,-1)
}

##Fonctions valeur régions

def valeur1(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 1 soit 0'''
    return 0

def valeur2(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 2 soit 0'''
    return 0

def valeur3(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 3 soit 4'''
    return 4

def valeur4(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 4 soit 0'''
    return 0

def valeur5(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 5 soit 2'''
    return 2

def valeur6(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 6 soit 0'''
    return 0

def valeur7(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 7 soit 0'''
    return 0

def valeur8(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 8 soit 0'''
    return 0

def valeur9(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 9 soit 5'''
    return 5

def valeur10(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 10 soit 3 par nuit'''
    return 3*comptage[5]

def valeur11(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 11 soit 2 par carte'''
    return 2*comptage[4]

def valeur12(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 12 soit 0'''
    return 0

def valeur13(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 13 soit 2 par pierre'''
    return 2*comptage[0]

def valeur14(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 14 soit 2 par nuit'''
    return 2*comptage[5]

def valeur15(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 15 soit 2 par animal'''
    return 2*comptage[1]

def valeur16(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 14 soit 2 par animal'''
    return 2*comptage[1]


def valeur17(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 17 soit 3 par pierre si 2 animaux'''
    if comptage[1]>=2:
        return 3*comptage[0]
    else :
        return 0

def valeur18(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 18 soit 10 par groupe de 4 couleurs'''
    m=min(comptage[6],comptage[7],comptage[8],comptage[9])                      #mininum de nombre de cartes regroupées en groupes de
                                                                                #couleur=le nombre de combianaisons de groupes de 4 cartes possible
    return m*10

def valeur19(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 19 soit 2 par plante'''
    return 2*comptage[2]

def valeur20(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 20 soit 2 par nuit si 1 pierre'''
    if comptage[0]>=1:
        return 2*comptage[5]
    else :
        return 0

def valeur21(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 21 soit 8 si 2 pierres'''
    if comptage[0]>=2:
        return 8
    else :
        return 0

def valeur22(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 22 soit 1 par carte'''
    return comptage[4]

def valeur23(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 23 soit 10 par groupe de 4 couleurs'''
    m=min(comptage[6],comptage[7],comptage[8],comptage[9])                      #mininum de nombre de cartes regroupées en groupes de
                                                                                #couleur=le nombre de combianaisons de groupes de 4 cartes possible
    return m*10

def valeur24(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 24 soit 2 par nuit si 1 animal'''
    if comptage[1]>=1:
        return 2*comptage[5]
    else :
        return 0

def valeur25(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 25 soit 1 par jaune et par verte'''
    return comptage[7]+comptage[8]

def valeur26(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 26 soit 3 par plante'''
    return 3*comptage[2]

def valeur27(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 27 soit 1 par jaune et par bleue'''
    return comptage[8]+comptage[9]

def valeur28(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 28 soit 3 par animal'''
    return 3*comptage[1]

def valeur29(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 29 soit 2 par plante'''
    return 2*comptage[2]

def valeur30(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 30 soit 2 par pierre'''
    return 2*comptage[0]

def valeur31(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 31 soit 1 par jaune et par rouge'''
    return comptage[6]+comptage[8]


def valeur32(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 32 soit 7 si 3 pierres'''
    if comptage[0]>=3:
        return 7
    else :
        return 0


def valeur33(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 33 soit 3 par plante'''
    return 3*comptage[2]

def valeur34(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 34 soit 3 par animal si 2 pierres'''
    if comptage[0]>=2:
        return 3*comptage[1]
    else :
        return 0


def valeur35(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 35 soit 10 par groupe de 4 couleurs'''
    m=min(comptage[6],comptage[7],comptage[8],comptage[9])                      #mininum de nombre de cartes regroupées en groupes de
                                                                                #couleur=le nombre de combianaisons de groupes de 4 cartes possible
    return m*10

def valeur36(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 36 soit 4 par plante si 2 animaux'''
    if comptage[1]>=2:
        return 4*comptage[2]
    else :
        return 0

def valeur37(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 37 soit 3 par nuit si 1 plante'''
    if comptage[2]>=1:
        return 5*comptage[5]
    else :
        return 0

def valeur38(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 38 soit 3 par carte si 1 animal et 1 plante'''
    if (comptage[1]>=1 and comptage[2]>=1):
        return 3*comptage[4]
    else :
        return 0

def valeur39(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 39 soit 9 si 2 animaux'''
    if comptage[1]>=2:
        return 9
    else :
        return 0

def valeur40(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 40 soit 3 par nuit si 1 pierre, 1 animal et 1 plante'''
    if (comptage[0]>=1 and comptage[1]>=1 and comptage[1]>=1):
        return 3*comptage[5]
    else :
        return 0


def valeur41(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 41 soit 4 par nuit si 2 pierres et 1 animal'''
    if (comptage[0]>=2 and comptage[1]>=1):
        return 4*comptage[5]
    else :
        return 0


def valeur42(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 42 soit 2 par jaune et verte si 1 pierre et 1 animal'''
    if (comptage[0]>=1 and comptage[1]>=1):
        return 2*(comptage[7]+comptage[8])
    else :
        return 0


def valeur43(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 43 soit 10 par groupe de 4 couleurs'''
    m=min(comptage[6],comptage[7],comptage[8],comptage[9])                      #mininum de nombre de cartes regroupées en groupes de
                                                                                #couleur=le nombre de combianaisons de groupes de 4 cartes possible
    return m*10

def valeur44(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 44 soit 2 par jaune et bleue si 1 pierre et 1 plante'''
    if (comptage[0]>=1 and comptage[2]>=1):
        return 2*(comptage[8]+comptage[9])
    else :
        return 0

def valeur45(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 45 soit 13 si 3 animaux'''
    if comptage[1]>=3:
        return 13
    else :
        return 0

def valeur46(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 46 soit 10 si 2 pierres et 1 animal'''
    if (comptage[0]>=2 and comptage[1]>=1):
        return 10
    else :
        return 0

def valeur47(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 47 soit 2 par jaune et rouge si 1 animal et 1 plante'''
    if (comptage[1]>=1 and comptage[2]>=1):
        return 2*(comptage[6]+comptage[8])
    else :
        return 0

def valeur48(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 48 soit 3 par pierre'''
    return 3*comptage[0]


def valeur49(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 49 soit 12 si 2 pierres et 1 plante'''
    if (comptage[0]>=2 and comptage[2]>=1):
        return 12
    else :
        return 0

def valeur50(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 50 soit 4 par verte si 2 plantes'''
    if comptage[2]>=2:
        return 4*comptage[7]
    else :
        return 0

def valeur51(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 51 soit 14 si 4 pierres'''
    if comptage[0]>=4:
        return 14
    else :
        return 0

def valeur52(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 52 soit 4 par animal si 3 pierres'''
    if comptage[0]>=3:
        return 4*comptage[1]
    else :
        return 0

def valeur53(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 53 soit 4 par rouge si 2 plantes'''
    if comptage[2]>=2:
        return 4*comptage[6]
    else :
        return 0

def valeur54(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 54 soit 4 par carte si 2 plantes'''
    if comptage[2]>=2:
        return 4*comptage[4]
    else :
        return 0


def valeur55(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 55 soit 3 par pierre si 1 animal et 2 plantes'''
    if (comptage[1]>=1 and comptage[2]>=2):
        return 3*comptage[0]
    else :
        return 0

def valeur56(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 56 soit 4 par bleue si 1 pierre et 2 animaux'''
    if (comptage[0]>=1 and comptage[1]>=2):
        return 4*comptage[9]
    else :
        return 0

def valeur57(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 57 soit 4 par pierre si 3 plantes'''
    if comptage[2]>=3:
        return 4*comptage[0]
    else :
        return 0


def valeur58(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 58 soit 3 par carte si 3 animaux'''
    if comptage[1]>=3:
        return 3*comptage[4]
    else :
        return 0

def valeur59(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 59 soit 3 par jaune et rouge si 1 pierre et 3 animaux'''
    if (comptage[0]>=1 and comptage[1]>=3):
        return 3*(comptage[6]+comptage[8])
    else :
        return 0

def valeur60(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 60 soit 16 si 2 pierres et 2 animaux'''
    if (comptage[0]>=2 and comptage[1]>=2):
        return 16
    else :
        return 0

def valeur61(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 61 soit 17 si 4 animaux'''
    if comptage[1]>=4:
        return 17
    else :
        return 0

def valeur62(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 62 soit 3 par jaune et bleue si 3 plantes '''
    if comptage[2]>=3:
        return 3*(comptage[8]+comptage[9])
    else :
        return 0

def valeur63(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 63 soit 15 si 2 animaux et 1 plante'''
    if (comptage[1]>=2 and comptage[2]>=1):
        return 15
    else :
        return 0

def valeur64(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 64 soit 18 si 2 pierres et 2 plantes'''
    if (comptage[0]>=2 and comptage[2]>=2):
        return 18
    else :
        return 0


def valeur65(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 65 soit 3 par jaune et verte si 3 plantes'''
    if comptage[2]>=3:
        return 3*(comptage[7]+comptage[8])
    else :
        return 0

def valeur66(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 66 soit 20 si 4 pierres'''
    if comptage[0]>=4:
        return 20
    else :
        return 0

def valeur67(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 67 soit 19 si 2 animaux et 2 plantes'''
    if (comptage[1]>=2 and comptage[2]>=2):
        return 19
    else :
        return 0

def valeur68(comptage:dict)->int:
    '''renvoie la valeur rapportée par la carte 68 soit 24 si 5 pierres'''
    if comptage[0]>=5:
        return 24
    else :
        return 0



valeur = {
    1 : valeur1,
    2 : valeur2,
    3 : valeur3,
    4 : valeur4,
    5 : valeur5,
    6 : valeur6,
    7 : valeur7,
    8 : valeur8,
    9 : valeur9,
    10 : valeur10,
    11 : valeur11,
    12 : valeur12,
    13 : valeur13,
    14 : valeur14,
    15 : valeur15,
    16 : valeur16,
    17 : valeur17,
    18 : valeur18,
    19 : valeur19,
    20 : valeur20,
    21 : valeur21,
    22 : valeur22,
    23 : valeur23,
    24 : valeur24,
    25 : valeur25,
    26 : valeur26,
    27 : valeur27,
    28 : valeur28,
    29 : valeur29,
    30 : valeur30,
    31 : valeur31,
    32 : valeur32,
    33 : valeur33,
    34 : valeur34,
    35 : valeur35,
    36 : valeur36,
    37 : valeur37,
    38 : valeur38,
    39 : valeur39,
    40 : valeur40,
    41 : valeur41,
    42 : valeur42,
    43 : valeur43,
    44 : valeur44,
    45 : valeur45,
    46 : valeur46,
    47 : valeur47,
    48 : valeur48,
    49 : valeur49,
    50 : valeur50,
    51 : valeur51,
    52 : valeur52,
    53 : valeur53,
    54 : valeur54,
    55 : valeur55,
    56 : valeur56,
    57 : valeur57,
    58 : valeur58,
    59 : valeur59,
    60 : valeur60,
    61 : valeur61,
    62 : valeur62,
    63 : valeur63,
    64 : valeur64,
    65 : valeur65,
    66 : valeur66,
    67 : valeur67,
    68 : valeur68
}


##Fonctions valeur sanctuaires


def val_sanctu1(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 1 soit 1 par carte'''
    return comptage[4]

def val_sanctu2(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 2 soit 1 par verte et jaune'''
    return comptage[7]+comptage[8]

def val_sanctu3(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 3 soit 0'''
    return 0

def val_sanctu4(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 4 soit 1 par carte'''
    return comptage[4]

def val_sanctu5(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 5 soit 0'''
    return 0

def val_sanctu6(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 6 soit 0'''
    return 0

def val_sanctu7(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 7 soit 1 par rouge et bleue'''
    return comptage[6]+comptage[9]

def val_sanctu8(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 8 soit 0'''
    return 0

def val_sanctu9(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 9 soit 1 par nuit'''
    return comptage[5]

def val_sanctu10(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 10 soit 0'''
    return 0

def val_sanctu11(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 11 soit 0'''
    return 0

def val_sanctu12(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 12 soit 1 par animal'''
    return comptage[1]

def val_sanctu13(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 13 soit 1 par plante'''
    return comptage[2]

def val_sanctu14(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 14 soit 1 par carte'''
    return comptage[4]

def val_sanctu15(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 15 soit 1 par rouge et jaune'''
    return comptage[6]+comptage[8]

def val_sanctu16(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 16 soit 4 par groupe de 4 couleurs'''
    m=min(comptage[6],comptage[7],comptage[8],comptage[9])                      #mininum de nombre de cartes regroupées en groupes de
                                                                                #couleur=le nombre de combianaisons de groupes de 4 cartes possible
    return m*4

def val_sanctu17(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 17 soit 2 par carte'''
    return 2*comptage[4]

def val_sanctu18(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 18 soit 2 par plante'''
    return 2*comptage[2]

def val_sanctu19(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 19 soit 5'''
    return 5

def val_sanctu20(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 20 soit 2 par pierre'''
    return 2*comptage[0]

def val_sanctu21(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 21 soit 1 par jaune et verte'''
    return comptage[7]+comptage[8]

def val_sanctu22(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 22 soit 1 par verte et rouge'''
    return comptage[6]+comptage[7]

def val_sanctu23(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 23 soit 1 par verte et bleue'''
    return comptage[7]+comptage[9]

def val_sanctu24(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 24 soit 4 par groupe de 4 couleurs'''
    m=min(comptage[6],comptage[7],comptage[8],comptage[9])                      #mininum de nombre de cartes regroupées en groupes de
                                                                                #couleur=le nombre de combianaisons de groupes de 4 cartes possible
    return m*4


def val_sanctu25(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 25 soit 1 par carte'''
    return comptage[4]

def val_sanctu26(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 26 soit 0'''
    return 0

def val_sanctu27(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 27 soit 0'''
    return 0

def val_sanctu28(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 28 soit 1 par jaune'''
    return comptage[8]

def val_sanctu29(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 29 soit 0'''
    return 0

def val_sanctu30(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 30 soit 0'''
    return 0

def val_sanctu31(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 31 soit 1 par rouge'''
    return comptage[6]

def val_sanctu32(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 32 soit 0'''
    return 0

def val_sanctu33(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 33 soit 0'''
    return 0

def val_sanctu34(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 34 soit 0'''
    return 0

def val_sanctu35(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 35 soit 0'''
    return 0

def val_sanctu36(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 36 soit 1 par nuit'''
    return comptage[5]

def val_sanctu37(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 37 soit 0'''
    return 0

def val_sanctu38(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 38 soit 1 par verte'''
    return comptage[7]

def val_sanctu39(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 39 soit 0'''
    return 0

def val_sanctu40(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 40 soit 0'''
    return 0

def val_sanctu41(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 41 soit 1 par bleue'''
    return comptage[9]

def val_sanctu42(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 42 soit 0'''
    return 0

def val_sanctu43(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 43 soit 0'''
    return 0

def val_sanctu44(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 44 soit 1 par pierre'''
    return comptage[0]

def val_sanctu45(comptage:dict)->int:
    '''renvoie la valeur rapportée par le sanctuaire 45 soit 2 par animal'''
    return 2*comptage[1]



#dictionnaire des valeurs sanctuaire
val_sanctu = {
    1  : val_sanctu1,
    2  : val_sanctu2,
    3  : val_sanctu3,
    4  : val_sanctu4,
    5  : val_sanctu5,
    6  : val_sanctu6,
    7  : val_sanctu7,
    8  : val_sanctu8,
    9  : val_sanctu9,
    10 : val_sanctu10,
    11 : val_sanctu11,
    12 : val_sanctu12,
    13 : val_sanctu13,
    14 : val_sanctu14,
    15 : val_sanctu15,
    16 : val_sanctu16,
    17 : val_sanctu17,
    18 : val_sanctu18,
    19 : val_sanctu19,
    20 : val_sanctu20,
    21 : val_sanctu21,
    22 : val_sanctu22,
    23 : val_sanctu23,
    24 : val_sanctu24,
    25 : val_sanctu25,
    26 : val_sanctu26,
    27 : val_sanctu27,
    28 : val_sanctu28,
    29 : val_sanctu29,
    30 : val_sanctu30,
    31 : val_sanctu31,
    32 : val_sanctu32,
    33 : val_sanctu33,
    34 : val_sanctu34,
    35 : val_sanctu35,
    36 : val_sanctu36,
    37 : val_sanctu37,
    38 : val_sanctu38,
    39 : val_sanctu39,
    40 : val_sanctu40,
    41 : val_sanctu41,
    42 : val_sanctu42,
    43 : val_sanctu43,
    44 : val_sanctu44,
    45 : val_sanctu45,

}

comptage = { 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}

def init(d:dict, S:list)->None:
    '''initialisation du dictionnaire de comptage avec les sanctuaires'''
    #remise à 0 de toutes les valeurs du dico
    for i in range(10):
        d[i]=0
    #pour chaque sanctuaire, ajout des attributs au dictionnaire
    for sanctuaire in S:
        #d'abord les attributs pierre, animal, plante
        if sanctuaires[sanctuaire][0]==0:
            d[0]+=1
        elif sanctuaires[sanctuaire][0]==1:
            d[1]+=1
        elif sanctuaires[sanctuaire][0]==2:
            d[2]+=1
        #ensuite les attributs nuit et carte
        if sanctuaires[sanctuaire][1]==0:
            d[5]+=1
        elif sanctuaires[sanctuaire][1]==1:
            d[4]+=1
        #enfin, les couleurs
        if sanctuaires[sanctuaire][2]==0:
            d[6]+=1
        elif sanctuaires[sanctuaire][2]==1:
            d[7]+=1
        elif sanctuaires[sanctuaire][2]==2:
            d[8]+=1
        elif sanctuaires[sanctuaire][2]==3:
            d[9]+=1
    #fin de l'initialisation avec les sanctuaires

def actualiser_comptage(d:dict, carte:int)->None:
    '''actualise le dictionnaire de comptage avec la nouvelle carte spécifiée'''
    #d'abord les attributs pierre, animal, plante
    d[0]+=regions[carte][0]
    d[1]+=regions[carte][1]
    d[2]+=regions[carte][2]
    #ensuite les attributs nuit et jour
    if regions[carte][3]==0:
        d[5]+=1
    elif regions[carte][3]==1:
        d[3]+=1
    #enfin, les couleurs
    d[regions[carte][5]+6]+=1
    #fin de l'actualisation

def score(J:list,d:dict)->list:
    '''fonction qui calcule le score d'un joueur et qui renvoie la liste des points gagnés par région et grâce aux sanctuaires, à la façon de la méthode de comptage des points dans le jeu'''
    R=J[1]                                                                      #liste des cartes région
    S=J[0]                                                                      #liste des cartes sanctuaire
    score=[]                                                                    #liste qui contiendra le score du joueur
    init(d, S)                                                                  #on initialise le dictionnaire de comptage
    for region in R:
        actualiser_comptage(d,region)
        score.append(valeur[region](d))
    #reste à compter les sanctuaires
    points_sanctuaire=0                                                         #initialisation des points rapportés par le sanctuaire
    for sanctuaire in S:
        points_sanctuaire+=val_sanctu[sanctuaire](d)
    score.append(points_sanctuaire)                                             #on ajoute les points rapportés par les sanctuaires au score
    score.append(sum(score))                                                    #ajout du total à la fin du score

    return score

def tri_classement(L:list)->list:
    '''fonction qui renvoie la liste des index classés par score décroissant'''
    # Associer chaque élément à son index initial
    index_list = list(range(len(L)))

    # Trier en conservant les index
    sorted_indices = sorted(index_list, key=lambda i: L[i], reverse=True)

    return sorted_indices


def partie(M : list)->list:
    '''fonction qui calcule la liste resultat à renvoyer pour avoir touos les résultats de la partie'''
                                                                                #on extrait les listes joueur de M
    nb_joueur = len(M)                                                          #nombre de joueurs
    L_scores=[]                                                                 #liste qui contiendra les scores de chaque joueur dans le
                                                                                #sens d'entrée des joueurs
    for J in M :
        L_scores.append(score(J,comptage))                                             #on ajoute un à un les scores de chaque joueur
    L_totaux = [L_scores[i][9] for i in range(nb_joueur)]                       #on prend les totaux des scores de chaque joueur
    classement = tri_classement(L_totaux)
    resultat=[classement,L_scores]
    return resultat


J1 = [[39,26,61,47,36,31,41,21],[6,8,15,16,33]]