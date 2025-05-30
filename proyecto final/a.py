import pygame
import sys

pygame.init()
AN, AL = 800, 600
P = pygame.display.set_mode((AN, AL))
pygame.display.set_caption("Pantalla de inicio")
clock = pygame.time.Clock()

# Estado del juego
estado = "menu"

# Botón
boton_rect = pygame.Rect(AN // 2 - 100, AL // 2 - 25, 200, 50)
fuente = pygame.font.SysFont(None, 40)

# Fondo y jugador (cargados solo si se entra al juego)
fondo = pygame.image.load("pixel_image_proportional_3200x2400.png").convert()
mapa_ancho, mapa_alto = fondo.get_size()
cuadro_ancho, cuadro_alto = 50, 50
C = pygame.Rect(
    mapa_ancho // 2 - cuadro_ancho // 2,
    mapa_alto // 2 - cuadro_alto // 2,
    cuadro_ancho,
    cuadro_alto
)
V = 5

# Bucle principal
while True:
    for E in pygame.event.get():
        if E.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif E.type == pygame.MOUSEBUTTONDOWN and estado == "menu":
            if boton_rect.collidepoint(E.pos):
                estado = "jugando"

    # ----------------------
    # ESTADO: MENÚ PRINCIPAL
    # ----------------------
    if estado == "menu":
        P.fill((20, 20, 20))

        # Botón "Jugar"
        pygame.draw.rect(P, (0, 100, 200), boton_rect)
        texto_jugar = fuente.render("Jugar", True, (255, 255, 255))
        texto_jugar_rect = texto_jugar.get_rect(center=boton_rect.center)
        P.blit(texto_jugar, texto_jugar_rect)

        # Botón "Salir"
        boton_salir_rect = pygame.Rect(AN // 2 - 100, AL // 2 + 50, 200, 50)
        pygame.draw.rect(P, (200, 0, 0), boton_salir_rect)
        texto_salir = fuente.render("Salir", True, (255, 255, 255))
        texto_salir_rect = texto_salir.get_rect(center=boton_salir_rect.center)
        P.blit(texto_salir, texto_salir_rect)

        # Detección de clics (debe estar en el bucle de eventos)
        if pygame.mouse.get_pressed()[0]:  # Botón izquierdo
            mouse_pos = pygame.mouse.get_pos()
            if boton_salir_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()


    # ----------------------
    # ESTADO: JUGANDO
    # ----------------------
    elif estado == "jugando":
        # Movimiento
        T = pygame.key.get_pressed()
        if T[pygame.K_w] or T[pygame.K_UP]:
            C.y -= V
        if T[pygame.K_s] or T[pygame.K_DOWN]:
            C.y += V
        if T[pygame.K_a] or T[pygame.K_LEFT]:
            C.x -= V
        if T[pygame.K_d] or T[pygame.K_RIGHT]:
            C.x += V
        if T[pygame.K_ESCAPE]:
            estado="menu"
        # Límites del mapa
        C.x = max(0, min(C.x, mapa_ancho - C.width))
        C.y = max(0, min(C.y, mapa_alto - C.height))

        # Cámara
        cam_x = C.x - AN // 2 + C.width // 2
        cam_y = C.y - AL // 2 + C.height // 2
        cam_x = max(0, min(cam_x, mapa_ancho - AN))
        cam_y = max(0, min(cam_y, mapa_alto - AL))

        # Dibujar mundo
        P.blit(fondo, (-cam_x, -cam_y))
        jugador_pantalla = pygame.Rect(C.x - cam_x, C.y - cam_y, C.width, C.height)
        pygame.draw.rect(P, (128, 0, 128), jugador_pantalla)

    pygame.display.flip()
    clock.tick(60)