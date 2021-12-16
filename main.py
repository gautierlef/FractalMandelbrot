import pygame


def draw_mandelbrot(option):
    MAX_ITERATION = 50  # Itérations maximales avant de considérer que la suite converge
    # Bornes
    if option == 1:
        XMIN, XMAX, YMIN, YMAX = -2, 0.5, -1.25, 1.25
    elif option == 2:
        XMIN, XMAX, YMIN, YMAX = -1.8, -1.7, -0.05, 0.05
    else:
        XMIN, XMAX, YMIN, YMAX = -1, 1, -1, 1
    LARGEUR, HAUTEUR = 650, 650
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Mandelbrot")
    # invertBlue = False
    invertRed = False
    red = 50
    for y in range(HAUTEUR):
        '''if y % 100 == 0:
            invertBlue = not invertBlue'''
        for x in range(LARGEUR):
            cx = (x * (XMAX - XMIN) / LARGEUR + XMIN)
            cy = (y * (YMIN - YMAX) / HAUTEUR + YMAX)
            xn = 0
            yn = 0
            n = 0
            while (xn * xn + yn * yn) < 4 and n < MAX_ITERATION:
                # Calcul des coordonnes de Mn
                tmp_x = xn
                tmp_y = yn
                xn = tmp_x * tmp_x - tmp_y * tmp_y + cx
                yn = 2 * tmp_x * tmp_y + cy
                n = n + 1
            if n == MAX_ITERATION:
                # Nuance de bleu pour l'intérieur - Non utilisé car moins beau
                '''if not invertBlue:
                    blue = y % 100 + 50
                else:
                    blue = (100 - y) % 100 + 50'''
                # Nuance de rouge pour l'intérieur
                if not invertRed:
                    red = red + 1
                else:
                    red = red - 1
                if red > 254 or red < 50:
                    invertRed = not invertRed
                green = 30
                blue = 30
                screen.set_at((x, y), (red, green, blue))
            else:
                # Nuance de gris pour l'extérieur
                grey = 255 * n / MAX_ITERATION
                screen.set_at((x, y), (grey, grey, grey))
        pygame.display.flip()
    loop = True
    # Boucle tant que la fenêtre n'est pas quittée
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
    pygame.quit()


# Menu de démarrage
pygame.init()
WIDTH = 650
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
smallfont = pygame.font.SysFont('Corbel', 35)
text1 = smallfont.render('Launch Mandelbrot 1', True, (255, 255, 255))
text2 = smallfont.render('Launch Mandelbrot 2', True, (255, 255, 255))
text3 = smallfont.render('Launch Mandelbrot 3', True, (255, 255, 255))
pygame.display.set_caption("Mandelbrot")
loop = True
while loop:
    screen.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()
    # Rectangle 1
    if 150 <= mouse[0] <= 150 + 400 and HEIGHT / 2 - 40 <= mouse[1] <= HEIGHT / 2:
        pygame.draw.rect(screen, (170, 170, 170), [150, HEIGHT / 2 - 40, 400, 40])
    else:
        pygame.draw.rect(screen, (100, 100, 100), [150, HEIGHT / 2 - 40, 400, 40])
    # Rectangle 2
    if 150 <= mouse[0] <= 150 + 400 and HEIGHT / 2 - 40 - 80 <= mouse[1] <= HEIGHT / 2 - 80:
        pygame.draw.rect(screen, (170, 170, 170), [150, HEIGHT / 2 - 40 - 80, 400, 40])
    else:
        pygame.draw.rect(screen, (100, 100, 100), [150, HEIGHT / 2 - 40 - 80, 400, 40])
    # Rectangle 3
    if 150 <= mouse[0] <= 150 + 400 and HEIGHT / 2 - 40 - 160 <= mouse[1] <= HEIGHT / 2 - 160:
        pygame.draw.rect(screen, (170, 170, 170), [150, HEIGHT / 2 - 40 - 160, 400, 40])
    else:
        pygame.draw.rect(screen, (100, 100, 100), [150, HEIGHT / 2 - 40 - 160, 400, 40])
    # Textes
    screen.blit(text3, (150 + 50, HEIGHT / 2 - 40))
    screen.blit(text2, (150 + 50, HEIGHT / 2 - 40 - 80))
    screen.blit(text1, (150 + 50, HEIGHT / 2 - 40 - 160))
    pygame.display.update()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            loop = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # Click rectangle 1
            if 150 <= mouse[0] <= 150 + 400 and HEIGHT / 2 - 40 <= mouse[1] <= HEIGHT / 2:
                pygame.quit()
                loop = False
                draw_mandelbrot(1)
            # Click rectangle 2
            if 150 <= mouse[0] <= 150 + 400 and HEIGHT / 2 - 40 - 80 <= mouse[1] <= HEIGHT / 2 - 80:
                pygame.quit()
                loop = False
                draw_mandelbrot(2)
            # Click rectangle 3
            if 150 <= mouse[0] <= 150 + 400 and HEIGHT / 2 - 40 - 160 <= mouse[1] <= HEIGHT / 2 - 160:
                pygame.quit()
                loop = False
                draw_mandelbrot(3)
