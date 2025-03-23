import pygame
import random

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
LARGEUR, HAUTEUR = 800, 600  # Taille de la fenêtre
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Yams")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (200, 0, 0)
GRIS = (150, 150, 150)
GRIS_CLAIR = (180, 180, 180)
BLEU = (0, 0, 255)

# Initialisation de la police
police = pygame.font.Font(None, 36)  # Police par défaut, taille 36

# Définition des rectangles de l'interface
grille_rect = pygame.Rect(50, 50, 500, 300)  # Grille de Yams
entree_rect = pygame.Rect(600, 50, 150, 50)  # Entrée utilisateur
selection_rect = pygame.Rect(50, 400, 500, 50)  # Sélection des dés
bouton_lancer_rect = pygame.Rect(600, 400, 50, 50)  # Bouton de lancement des dés

# Texte des boutons
texte_bouton = police.render("Lancer", True, NOIR)

# Initialisation des dés (valeurs et état de sélection)
des = [random.randint(1, 6) for _ in range(5)]  # 5 dés générés aléatoirement
des_selectionnes = [False] * 5  # État de sélection des dés

# Chargement des images des dés
dice_images = {i: pygame.image.load(f"de{i}.png") for i in range(1, 7)}

# Fonction pour lancer les dés
def lancer_des():
    for i in range(5):
        if not des_selectionnes[i]:  # Ne relance que les dés non sélectionnés
            des[i] = random.randint(1, 6)

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            # Vérifier si le bouton de lancement est cliqué
            if bouton_lancer_rect.collidepoint(x, y):
                lancer_des()
            
            # Vérifier si un dé est cliqué pour le sélectionner/désélectionner
            for i in range(5):
                de_rect = pygame.Rect(50 + i * 100, 400, 50, 50)
                if de_rect.collidepoint(x, y):
                    des_selectionnes[i] = not des_selectionnes[i]

    # Remplissage de l'écran
    screen.fill(BLANC)
    
    # Affichage des zones
    pygame.draw.rect(screen, GRIS, grille_rect)
    pygame.draw.rect(screen, GRIS_CLAIR, entree_rect)
    pygame.draw.rect(screen, GRIS, selection_rect)
    pygame.draw.rect(screen, ROUGE, bouton_lancer_rect)
    
    # Affichage du texte sur le bouton
    screen.blit(texte_bouton, (bouton_lancer_rect.x + (bouton_lancer_rect.width - texte_bouton.get_width()) // 2,
                               bouton_lancer_rect.y + (bouton_lancer_rect.height - texte_bouton.get_height()) // 2))
    
    # Affichage des dés
    for i in range(5):
        de_rect = pygame.Rect(50 + i * 100, 400, 50, 50)
        screen.blit(dice_images[des[i]], (de_rect.x, de_rect.y))
        if des_selectionnes[i]:
            pygame.draw.rect(screen, BLEU, de_rect, 3)  # Encadrer le dé sélectionné
    
    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()