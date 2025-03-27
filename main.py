import os
os.system('clear')
Joueur = [
    'Mamie',
    'Maman',
]

nb_j = input("Combien y'a t'il de joueur :")
for _ in range(int(nb_j)):
    os.system('clear')
    nom = input('Nom du joueur :')
    Joueur.append(nom)

regle = [
    '0-> 1',
    '1-> 2', 
    '2-> 3', 
    '3-> 4', 
    '4-> 5', 
    '5-> 6', 
    'Total Supèrieur',
    'Bonus si > à 62 [35]',
    '',
    '6-> Chance [total 5d]',
    '7-> Brelan(3d id.) [total]', 
    '8-> Carré(4d id.) [total]', 
    '9-> Full [25]', 
    '10-> Petit Suite [30]',
    '11-> Grande Suite [40]',
    "12-> Yam's [50 re +100]",
    'Total Infèrieur',
    '',
    'Total'
]

point = {}
for nom in Joueur:
    point[nom] = {}
    for figure in regle:
        point[nom][figure] = None

def un(joueur):
    resultat = input("Combien de dès pour " + joueur + ": ")
    point[joueur]['0-> 1'] = int(resultat)*1
    point[joueur]['Total Supèrieur'] += int(resultat)*1
    Bonus(joueur)
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])
    
def deux(joueur):
    resultat = input("Combien de dès pour " + joueur + ": ")
    point[joueur]['1-> 2'] = int(resultat)*2
    point[joueur]['Total Supèrieur'] += int(resultat)*2
    Bonus(joueur)
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def trois(joueur):
    resultat = input("Combien de dès pour " + joueur + ": ")
    point[joueur]['2-> 3'] = int(resultat)*3
    point[joueur]['Total Supèrieur'] += int(resultat)*3
    Bonus(joueur)
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def quatre(joueur):
    resultat = input("Combien de dès pour " + joueur + ": ")
    point[joueur]['3-> 4'] = int(resultat)*4
    point[joueur]['Total Supèrieur'] += int(resultat)*4
    Bonus(joueur)
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def cinq(joueur):
    resultat = input("Combien de dès pour " + joueur + ": ")
    point[joueur]['4-> 5'] = int(resultat)*5
    point[joueur]['Total Supèrieur'] += int(resultat)*5
    Bonus(joueur)
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def six(joueur):
    resultat = input("Combien de dès pour " + joueur + ": ")
    point[joueur]['5-> 6'] = int(resultat)*6
    point[joueur]['Total Supèrieur'] += int(resultat)*6
    Bonus(joueur)
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Chance(joueur):
    resultat = input("Combien a obtenue " + joueur + ": ")
    point[joueur]['6-> Chance [total 5d]'] = int(resultat)
    point[joueur]['Total Infèrieur'] += int(resultat)
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Brelan(joueur):
    resultat = input("Brelan de combien a obtenue " + joueur + ": ")
    point[joueur]['7-> Brelan(3d id.) [total]'] = int(resultat)*3
    point[joueur]['Total Infèrieur'] += int(resultat)*3
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Carré(joueur):
    resultat = input("Carré de combien a obtenue " + joueur + ": ")
    point[joueur]['8-> Carré(4d id.) [total]'] = int(resultat)*4
    point[joueur]['Total Infèrieur'] += int(resultat)*4
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Full(joueur):
    point[joueur]['9-> Full [25]'] = 25
    point[joueur]['Total Infèrieur'] += 25
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Petite_Suite(joueur):
    point[joueur]['10-> Petit Suite [30]'] = 30
    point[joueur]['Total Infèrieur'] += 30
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Grande_Suite(joueur):
    point[joueur]['11-> Grande Suite [40]'] = 40
    point[joueur]['Total Infèrieur'] += 40
    point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Yam_s(joueur):
    if point[joueur]["12-> Yam's [50 re +100]"] == 50:
        point[joueur]["12-> Yam's [50 re +100]"] += 100
        eliminer(joueur)
        point[joueur]['Total Infèrieur'] += 100
        point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

    else:
        point[joueur]["12-> Yam's [50 re +100]"] = 50
        point[joueur]['Total Infèrieur'] += 50
        point[joueur]['Total'] = (point[joueur]['Total Supèrieur'] + point[joueur]['Total Infèrieur'])

def Bonus(joueur):
    if point[joueur]['Total Supèrieur'] >= 62:
        point[joueur]['Bonus si > à 62 [35]'] = 35
        point[joueur]['Total Supèrieur'] += 35

def eliminer(joueur):
    choix = input('Quels figure ' + joueur + "doit éliminer :")
    if choix == '0':
        point[joueur]['0-> 1'] = 0

    elif choix == '1':
        point[joueur]['1-> 2'] = 0

    elif choix == '2':
        point[joueur]['2-> 3'] = 0

    elif choix == '3':
        point[joueur]['3-> 4'] = 0

    elif choix == '4':
        point[joueur]['4-> 5'] = 0

    elif choix == '5':
        point[joueur]['5-> 6'] = 0

    elif choix == '6':
        point[joueur]['6-> Chance [total 5d]'] = 0

    elif choix == '7':
        point[joueur]['7-> Brelan(3d id.) [total]'] = 0

    elif choix == '8':
        point[joueur]['8-> Carré(4d id.) [total]'] = 0

    elif choix == '9':
        point[joueur]['9-> Full [25]'] = 0

    elif choix == '10':
        point[joueur]['10-> Petit Suite [30]'] = 0

    elif choix == '11':
        point[joueur]['11-> Grande Suite [40]'] = 0

    elif choix == '12':
        point[joueur]["12-> Yam's [50 re +100]"] = 0

def Gagnant(joueur):
    for nom in joueur:
        pass

def max_mot(règle):
    max = 0
    for figure in règle:
        if len(figure) > max:
            max = len(figure)
    return max + 1

def max_joueur(joueur):
    max = 0
    lpl = ''
    for nom in joueur:
        if len(nom) > max:
            max = len(nom)
            lpl = nom
    if max%2 == 0:
        max += 1
    return max

def verificateur(ls_valide, partie):
    out = False 
    if partie == 0:
        while not out:
            resultat = input('Voulez-vous éliminer une figure(o/n) :')
            if resultat in ls_valide:
                out = True   
            else:
                print("Entrée non valide veuillez saisir une entrée correcte")            
    elif partie == 1:
        while not out:
            resultat = input("Choississez votre figure : ")
            if resultat in ls_valide:
                out = True
            else:
                print("Entrée non valide veuillez saisir une entrée correcte")  
    return resultat
            

def initialisation(joueur):
    for nom in joueur:
        point[nom]['Total Supèrieur'] = 0
        point[nom]['Bonus si > à 62 [35]'] = 0
        point[nom]['Total Infèrieur'] = 0
        point[nom]['Total'] = 0 

def constructeur_de_ligne(joueur, figure, lg_dess, lg_hb, lg_dess_joueur):
    resultat = "+" + lg_dess*'-' + lg_hb + '\n' + "| " + figure + (lg_dess - 1 - len(figure))*' ' + '|'
    for nom in joueur:
        carac = str(point[nom][figure])
        if point[nom][figure] == None:
            resultat = resultat + ((2+lg_dess_joueur)*' ' + '|')
        elif len(carac) == 1:
            resultat = resultat + (((2+lg_dess_joueur//2) - 1)*' ' + carac + ((2+lg_dess_joueur//2) - 1)*' ' + '|')
        elif len(carac) == 2:
            resultat = resultat + (((2+lg_dess_joueur//2) - 2)*' ' + carac + ((2+lg_dess_joueur//2) - 1)*' ' + '|')
        elif len(carac) == 3:
            resultat = resultat + (((2+lg_dess_joueur//2) - 2)*' ' + carac + ((2+lg_dess_joueur//2) - 2)*' ' + '|')
        
    print(resultat)

def interface(règle,joueur):
    lg_dess = max_mot(règle)
    lg_dess_joueur = max_joueur(joueur)
    lg_joueur = ''
    lg_hb = ''
    for nom in joueur:
        reste = lg_dess_joueur - len(nom)
        if nom != joueur[-1]:
            lg_joueur = lg_joueur + (' | ' + nom + reste*' ')
        else:
            lg_joueur = lg_joueur + (' | ' + nom + reste*' ' + ' |')
    for nom in joueur:
        if nom != joueur[-1]:
            lg_hb = lg_hb + ('+' + (lg_dess_joueur+2)*'-')
        else:
            lg_hb = lg_hb + ('+' + (lg_dess_joueur+2)*'-' + '+')
    print((lg_dess + 1)*' ' + lg_hb)
    print((lg_dess)*' ' + lg_joueur)
    for i in range(len(règle)):
        if règle[i] != '' :
            constructeur_de_ligne(joueur, règle[i], lg_dess, lg_hb, lg_dess_joueur)    
        else:
            print("+" + lg_dess*'-' + lg_hb + '\n')
    print("+" + lg_dess*'-' + lg_hb)

def lancement_du_jeu(regle, joueur):
    initialisation(joueur)
    for tour in range(13):
        for nom in joueur:
            os.system('clear')
            interface(regle,Joueur)
            print("C'est au tour de " + nom)
            resultat = verificateur(["o", "n"], 0)
            if resultat == 'n':
                choix= verificateur(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], 1)
                if choix == "0":
                    os.system('clear')
                    un(nom)
                elif choix == "1":
                    os.system('clear')
                    deux(nom)
                elif choix == "2": 
                    os.system('clear')
                    trois(nom)
                elif choix == "3":
                    os.system('clear')
                    quatre(nom)
                elif choix == "4":
                    os.system('clear')
                    cinq(nom)
                elif choix == "5":
                    os.system('clear')
                    six(nom)
                elif choix == "6":
                    os.system('clear')
                    Chance(nom)
                elif choix == "7":
                    os.system('clear')
                    Brelan(nom)
                elif choix == "8":
                    os.system('clear')
                    Carré(nom)
                elif choix == "9":
                    os.system('clear')
                    Full(nom)
                elif choix == "10":
                    os.system('clear')
                    Petite_Suite(nom)
                elif choix == "11":
                    os.system('clear')
                    Grande_Suite(nom)
                elif choix == "12":
                    os.system('clear')
                    Yam_s(nom)
            elif resultat == 'o':
                eliminer(nom)
                
    os.system('clear')
    interface(regle, joueur)
    print('La partie est finit !!!')
    print("Le gagnant est : " + Gagnant(joueur))
lancement_du_jeu(regle, Joueur)
