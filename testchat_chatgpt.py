import pygame
from random import randint

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
LARGEUR, HAUTEUR = 1200, 900
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Yams")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (200, 0, 0)
GRIS = (150, 150, 150)
GRIS_CLAIR = (180, 180, 180)
BLEU = (0, 0, 255)
VERT = (100, 200, 100)

# Initialisation de la police
police = pygame.font.Font(None, 36)

# Taille des dés
TAILLE_DE = 120
ESPACEMENT_DE = 20

# Chargement des images des dés
des_images = [pygame.image.load(f"Face_{i+1}.png") for i in range(6)]

# Définition des rectangles de l'interface
grille_rect = pygame.Rect(50, 50, 700, 500)
entree_rect = pygame.Rect(800, 50, 150, 50)
selection_rect = pygame.Rect(50, 600, 700, 140)
bouton_lancer_rect = pygame.Rect(800, 600, 150, 50)

# Création de la grille dynamique
grille_cases = []
noms_joueurs = ["Joueur 1", "Joueur 2", "Joueur 3", "Joueur 4"]
nombre_joueurs = len(noms_joueurs)
largeur_case = 100
hauteur_case = 40

for ligne in range(14):
    row = []
    for colonne in range(nombre_joueurs):
        rect = pygame.Rect(200 + colonne * largeur_case, 100 + ligne * hauteur_case, largeur_case, hauteur_case)
        row.append(rect)
    grille_cases.append(row)

# Calcul des positions des dés
positions_des = [
    (50 + i * (TAILLE_DE + ESPACEMENT_DE), 620)
    for i in range(5)
]

des_valeurs = [0, 0, 0, 0, 0]
des_selectionnes = [False] * 5

# Texte des boutons
texte_bouton = police.render("Lancer", True, NOIR)

# Texte des catégories
titres_categories = [
    "Total de 1", "Total de 2", "Total de 3", "Total de 4", "Total de 5", "Total de 6", "Bonus", "Brelan",
    "Carré", "Full House", "Petite Suite", "Grande Suite", "Yams", "Chance"
]

# Gestion de l'entrée utilisateur
valeur_saisie = ""
case_selectionnee = None

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Vérifier si une case de la grille est cliquée
            for i, ligne in enumerate(grille_cases):
                for j, case in enumerate(ligne):
                    if case.collidepoint(x, y):
                        case_selectionnee = (i, j)
            # Vérifier si on clique sur le bouton lancer
            if bouton_lancer_rect.collidepoint(x, y):
                for i in range(5):
                    if not des_selectionnes[i]:
                        des_valeurs[i] = randint(1, 6)
        elif event.type == pygame.KEYDOWN:
            if case_selectionnee:
                if event.key == pygame.K_BACKSPACE:
                    valeur_saisie = valeur_saisie[:-1]
                elif event.key == pygame.K_RETURN:
                    case_selectionnee = None
                else:
                    valeur_saisie += event.unicode
    
    screen.fill(BLANC)
    pygame.draw.rect(screen, GRIS, grille_rect)
    pygame.draw.rect(screen, GRIS_CLAIR, entree_rect)
    pygame.draw.rect(screen, GRIS, selection_rect)
    pygame.draw.rect(screen, ROUGE, bouton_lancer_rect)
    
    screen.blit(texte_bouton, (bouton_lancer_rect.x + (bouton_lancer_rect.width - texte_bouton.get_width()) // 2,
                               bouton_lancer_rect.y + (bouton_lancer_rect.height - texte_bouton.get_height()) // 2))
    
    # Dessin des dés
    for i, pos in enumerate(positions_des):
        if des_valeurs[i] > 0:
            screen.blit(des_images[des_valeurs[i] - 1], pos)
        else:
            pygame.draw.rect(screen, BLEU, (pos[0], pos[1], TAILLE_DE, TAILLE_DE))
        if des_selectionnes[i]:
            pygame.draw.rect(screen, NOIR, (pos[0], pos[1], TAILLE_DE, TAILLE_DE), 5)
    
    # Dessin des catégories et des cases
    for i, ligne in enumerate(grille_cases):
        texte = police.render(titres_categories[i], True, NOIR)
        screen.blit(texte, (50, 110 + i * hauteur_case))
        for j, case in enumerate(ligne):
            pygame.draw.rect(screen, NOIR, case, 2)
            if case_selectionnee == (i, j) and valeur_saisie:
                texte_valeur = police.render(valeur_saisie, True, NOIR)
                screen.blit(texte_valeur, (case.x + 10, case.y + 5))
    
    # Affichage des noms des joueurs
    for j, nom in enumerate(noms_joueurs):
        texte_nom = police.render(nom, True, NOIR)
        screen.blit(texte_nom, (200 + j * largeur_case, 70))
    
    pygame.display.flip()

pygame.quit()