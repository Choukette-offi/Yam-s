import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
LARGEUR, HAUTEUR = 800, 600  # Taille de la fenêtre
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Première fenêtre Pygame")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (200, 0, 0)
GRIS = (150, 150, 150)
GRIS_CLAIR = (180, 180, 180)
GRIS_FONCE = (100, 100, 100)

# Initialisation de la police
police = pygame.font.Font(None, 36)  # Police par défaut, taille 36

# Définition du bouton mobile
bouton_rect = pygame.Rect(300, 400, 200, 50)
texte_bouton = police.render("Clique ici", True, NOIR)
couleur_bouton = GRIS
vitesse_bouton = 2

defiler_droite = True  # Direction du mouvement

# Champ de texte
input_rect = pygame.Rect(250, 200, 300, 50)
texte_utilisateur = ""
saisie_active = False

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if saisie_active:
                if event.key == pygame.K_RETURN:
                    print("Texte saisi :", texte_utilisateur)
                    texte_utilisateur = ""  # Réinitialiser après validation
                elif event.key == pygame.K_BACKSPACE:
                    texte_utilisateur = texte_utilisateur[:-1]
                else:
                    texte_utilisateur += event.unicode
            print("Touche pressée : " + pygame.key.name(event.key))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_rect.collidepoint(event.pos):
                print("Bouton cliqué !")
            if input_rect.collidepoint(event.pos):
                saisie_active = True
            else:
                saisie_active = False
        if event.type == pygame.MOUSEMOTION:
            if bouton_rect.collidepoint(event.pos):
                couleur_bouton = GRIS_CLAIR  # Change la couleur si la souris est dessus
            else:
                couleur_bouton = GRIS  # Revient à la couleur de base sinon
    
    # Déplacement du bouton
    if defiler_droite:
        bouton_rect.x += vitesse_bouton
        if bouton_rect.right >= LARGEUR:
            defiler_droite = False
    else:
        bouton_rect.x -= vitesse_bouton
        if bouton_rect.left <= 0:
            defiler_droite = True
    
    # Remplissage de l'écran
    screen.fill(BLANC)
    
    # Affichage du texte
    texte = police.render("Appuie sur une touche", True, NOIR)
    screen.blit(texte, (LARGEUR // 2 - texte.get_width() // 2, 50))
    
    # Ombre du bouton
    ombre_rect = bouton_rect.move(5, 5)
    pygame.draw.rect(screen, GRIS_FONCE, ombre_rect)
    
    # Affichage du bouton avec couleur dynamique
    pygame.draw.rect(screen, couleur_bouton, bouton_rect)
    screen.blit(texte_bouton, (bouton_rect.x + (bouton_rect.width - texte_bouton.get_width()) // 2,
                               bouton_rect.y + (bouton_rect.height - texte_bouton.get_height()) // 2))
    
    # Affichage du champ de texte
    pygame.draw.rect(screen, GRIS, input_rect, 2)
    texte_surface = police.render(texte_utilisateur, True, NOIR)
    screen.blit(texte_surface, (input_rect.x + 5, input_rect.y + 10))
    
    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
