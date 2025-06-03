import pygame
import sys
import math
import random

pygame.init()
AN, AL = 800, 600
P = pygame.display.set_mode((AN, AL))
pygame.display.set_caption("Pantalla de inicio")
clock = pygame.time.Clock()

estado = "menu"

boton_rect = pygame.Rect(AN // 2 - 100, AL // 2 - 25, 200, 50)
fuente = pygame.font.SysFont(None, 40)

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

ENEMIGOS = []
VELOCIDAD_ENEMIGO = 3
ULTIMA_CREACION = pygame.time.get_ticks()
INTERVALO_CREACION = 6000

BITS = []
TIEMPO_ULTIMO_BIT = pygame.time.get_ticks()
INTERVALO_BITS = 5000

vida = 100
ultimo_daño = pygame.time.get_ticks()

def crear_enemigo():
    x = random.randint(0, mapa_ancho - cuadro_ancho)
    y = random.randint(0, mapa_alto - cuadro_alto)
    enemigo = pygame.Rect(x, y, cuadro_ancho, cuadro_alto)
    ENEMIGOS.append(enemigo)

def mover_hacia_jugador(enemigo):
    dx = C.centerx - enemigo.centerx
    dy = C.centery - enemigo.centery
    distancia = math.hypot(dx, dy)
    if distancia != 0:
        dx /= distancia
        dy /= distancia
        enemigo.x += int(dx * VELOCIDAD_ENEMIGO)
        enemigo.y += int(dy * VELOCIDAD_ENEMIGO)

def evitar_superposicion():
    for i in range(len(ENEMIGOS)):
        for j in range(i + 1, len(ENEMIGOS)):
            e1, e2 = ENEMIGOS[i], ENEMIGOS[j]
            if e1.colliderect(e2):
                dx = e1.centerx - e2.centerx
                dy = e1.centery - e2.centery
                distancia = math.hypot(dx, dy) or 1
                separacion = 5
                moverx = (dx / distancia) * separacion
                movery = (dy / distancia) * separacion
                e1.x += int(moverx)
                e1.y += int(movery)
                e2.x -= int(moverx)
                e2.y -= int(movery)

while True:
    for E in pygame.event.get():
        if E.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif E.type == pygame.MOUSEBUTTONDOWN:
            if estado == "menu":
                if boton_rect.collidepoint(E.pos):
                    estado = "jugando"
                boton_salir_rect = pygame.Rect(AN // 2 - 100, AL // 2 + 50, 200, 50)
                if boton_salir_rect.collidepoint(E.pos):
                    pygame.quit()
                    sys.exit()
            elif estado == "game_over":
                boton_reiniciar_rect = pygame.Rect(AN // 2 - 100, AL // 2 - 25, 200, 50)
                boton_salir_rect = pygame.Rect(AN // 2 - 100, AL // 2 + 50, 200, 50)
                if boton_reiniciar_rect.collidepoint(E.pos):
                    # Reiniciar variables para empezar de nuevo
                    ENEMIGOS.clear()
                    BITS.clear()
                    vida = 100
                    C.x = mapa_ancho // 2 - cuadro_ancho // 2
                    C.y = mapa_alto // 2 - cuadro_alto // 2
                    estado = "jugando"
                elif boton_salir_rect.collidepoint(E.pos):
                    pygame.quit()
                    sys.exit()

    if estado == "menu":
        P.fill((20, 20, 20))

        pygame.draw.rect(P, (0, 100, 200), boton_rect)
        texto_jugar = fuente.render("Jugar", True, (255, 255, 255))
        texto_jugar_rect = texto_jugar.get_rect(center=boton_rect.center)
        P.blit(texto_jugar, texto_jugar_rect)

        boton_salir_rect = pygame.Rect(AN // 2 - 100, AL // 2 + 50, 200, 50)
        pygame.draw.rect(P, (200, 0, 0), boton_salir_rect)
        texto_salir = fuente.render("Salir", True, (255, 255, 255))
        texto_salir_rect = texto_salir.get_rect(center=boton_salir_rect.center)
        P.blit(texto_salir, texto_salir_rect)

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if boton_salir_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    elif estado == "jugando":
        T = pygame.key.get_pressed()
        velocidad_actual = V

        tocando = any(C.colliderect(enemigo) for enemigo in ENEMIGOS)
        if tocando:
            velocidad_actual = V // 2

        if T[pygame.K_w] or T[pygame.K_UP]:
            C.y -= velocidad_actual
        if T[pygame.K_s] or T[pygame.K_DOWN]:
            C.y += velocidad_actual
        if T[pygame.K_a] or T[pygame.K_LEFT]:
            C.x -= velocidad_actual
        if T[pygame.K_d] or T[pygame.K_RIGHT]:
            C.x += velocidad_actual
        if T[pygame.K_ESCAPE]:
            estado = "menu"

        C.x = max(0, min(C.x, mapa_ancho - C.width))
        C.y = max(0, min(C.y, mapa_alto - C.height))

        cam_x = C.x - AN // 2 + C.width // 2
        cam_y = C.y - AL // 2 + C.height // 2
        cam_x = max(0, min(cam_x, mapa_ancho - AN))
        cam_y = max(0, min(cam_y, mapa_alto - AL))

        P.blit(fondo, (-cam_x, -cam_y))
        jugador_pantalla = pygame.Rect(C.x - cam_x, C.y - cam_y, C.width, C.height)
        pygame.draw.rect(P, (128, 0, 128), jugador_pantalla)

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ULTIMA_CREACION >= INTERVALO_CREACION:
            crear_enemigo()
            crear_enemigo()
            ULTIMA_CREACION = tiempo_actual

        for enemigo in ENEMIGOS:
            mover_hacia_jugador(enemigo)

        evitar_superposicion()

        for enemigo in ENEMIGOS:
            enemigo_pantalla = pygame.Rect(
                enemigo.x - cam_x, enemigo.y - cam_y, enemigo.width, enemigo.height)
            pygame.draw.rect(P, (255, 0, 0), enemigo_pantalla)

        if tiempo_actual - TIEMPO_ULTIMO_BIT >= INTERVALO_BITS:
            for enemigo in ENEMIGOS:
                dx = enemigo.centerx - C.centerx
                dy = enemigo.centery - C.centery
                distancia = math.hypot(dx, dy)
                if distancia != 0:
                    dx /= distancia
                    dy /= distancia
                    bit = pygame.Rect(C.centerx, C.centery, 10, 10)
                    BITS.append([bit, dx * 7, dy * 7])
                    break
            TIEMPO_ULTIMO_BIT = tiempo_actual

        for bit in BITS[:]:
            bit[0].x += bit[1]
            bit[0].y += bit[2]
            if not fondo.get_rect().contains(bit[0]):
                BITS.remove(bit)
                continue
            for enemigo in ENEMIGOS:
                if bit[0].colliderect(enemigo):
                    ENEMIGOS.remove(enemigo)
                    BITS.remove(bit)
                    break

        for bit, _, _ in BITS:
            
            bit_pantalla = pygame.Rect(bit.x - cam_x, bit.y - cam_y, bit.width, bit.height)
            pygame.draw.rect(P, (0, 255, 255), bit_pantalla)

        cantidad_colisiones = sum(1 for enemigo in ENEMIGOS if C.colliderect(enemigo))
        if cantidad_colisiones > 0 and tiempo_actual - ultimo_daño >= 2000:
            vida -= cantidad_colisiones * 5
            vida = max(vida, 0)
            ultimo_daño = tiempo_actual

        # Cuando la vida llega a 0 cambia el estado a game_over
        if vida <= 0:
            estado = "game_over"

        barra_anchura = 200
        barra_altura = 20
        barra_surface = pygame.Surface((barra_anchura, barra_altura))
        barra_surface.fill((100, 0, 0))
        pygame.draw.rect(barra_surface, (0, 255, 0), (0, 0, int(barra_anchura * (vida / 100)), barra_altura))
        P.blit(barra_surface, (10, AL - 30))

        minimapa_ancho, minimapa_alto = 200, 150
        minimapa = pygame.Surface((minimapa_ancho, minimapa_alto))
        minimapa.fill((40, 40, 40))

        escala_x = minimapa_ancho / mapa_ancho
        escala_y = minimapa_alto / mapa_alto

        jugador_mx = int(C.centerx * escala_x)
        jugador_my = int(C.centery * escala_y)
        pygame.draw.circle(minimapa, (0, 255, 0), (jugador_mx, jugador_my), 3)

        for enemigo in ENEMIGOS:
            ex = int(enemigo.centerx * escala_x)
            ey = int(enemigo.centery * escala_y)
            pygame.draw.circle(minimapa, (255, 0, 0), (ex, ey), 3)

        P.blit(minimapa, (AN - minimapa_ancho - 10, 10))

    elif estado == "game_over":
        P.fill((20, 20, 20))
        boton_reiniciar_rect = pygame.Rect(AN // 2 - 100, AL // 2 - 25, 200, 50)
        boton_salir_rect = pygame.Rect(AN // 2 - 100, AL // 2 + 50, 200, 50)

        pygame.draw.rect(P, (0, 100, 200), boton_reiniciar_rect)
        texto_reiniciar = fuente.render("Volver a jugar", True, (255, 255, 255))
        texto_reiniciar_rect = texto_reiniciar.get_rect(center=boton_reiniciar_rect.center)
        P.blit(texto_reiniciar, texto_reiniciar_rect)

        pygame.draw.rect(P, (200, 0, 0), boton_salir_rect)
        texto_salir = fuente.render("Salir", True, (255, 255, 255))
        texto_salir_rect = texto_salir.get_rect(center=boton_salir_rect.center)
        P.blit(texto_salir, texto_salir_rect)

    pygame.display.update()
    clock.tick(60)