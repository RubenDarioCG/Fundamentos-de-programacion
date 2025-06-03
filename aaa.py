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
radio_jugador = 25
C = {'x': mapa_ancho // 2, 'y': mapa_alto // 2, 'radio': radio_jugador}
V = 5

ENEMIGOS = []
VELOCIDAD_ENEMIGO = 3
ULTIMA_CREACION = pygame.time.get_ticks()
INTERVALO_CREACION = 6000
MAX_ENEMIGOS = 20
BITS = []
TIEMPO_ULTIMO_BIT = pygame.time.get_ticks()
INTERVALO_BITS = 4000  # Reducido para disparar con más frecuencia

vida = 100
ultimo_daño = pygame.time.get_ticks()

inicio_juego_tiempo = pygame.time.get_ticks()

def crear_enemigo():
    x = random.randint(0, mapa_ancho)
    y = random.randint(0, mapa_alto)
    enemigo = {'x': x, 'y': y, 'radio': 25, 'vx': 0, 'vy': 0}
    ENEMIGOS.append(enemigo)

def mover_hacia_jugador(enemigo):
    dx = C['x'] - enemigo['x']
    dy = C['y'] - enemigo['y']
    distancia = math.hypot(dx, dy)
    if distancia != 0:
        dx /= distancia
        dy /= distancia
        enemigo['vx'] = dx * VELOCIDAD_ENEMIGO
        enemigo['vy'] = dy * VELOCIDAD_ENEMIGO
        enemigo['x'] += enemigo['vx']
        enemigo['y'] += enemigo['vy']

def evitar_superposicion():
    for i in range(len(ENEMIGOS)):
        for j in range(i + 1, len(ENEMIGOS)):
            e1, e2 = ENEMIGOS[i], ENEMIGOS[j]
            dx = e1['x'] - e2['x']
            dy = e1['y'] - e2['y']
            distancia = math.hypot(dx, dy) or 1
            if distancia < e1['radio'] + e2['radio']:
                # Rebote: intercambiar velocidades (simplificado)
                e1['vx'], e2['vx'] = -e1['vx'], -e2['vx']
                e1['vy'], e2['vy'] = -e1['vy'], -e2['vy']
                e1['x'] += e1['vx']
                e1['y'] += e1['vy']
                e2['x'] += e2['vx']
                e2['y'] += e2['vy']

def colisiona_circulos(x1, y1, r1, x2, y2, r2):
    dx = x1 - x2
    dy = y1 - y2
    return math.hypot(dx, dy) < r1 + r2

elif estado == "jugando":
    T = pygame.key.get_pressed()
    velocidad_actual = V

    tocando = any(colisiona_circulos(C['x'], C['y'], C['radio'], e['x'], e['y'], e['radio']) for e in ENEMIGOS)
    if tocando:
        velocidad_actual = V // 2

    if T[pygame.K_w] or T[pygame.K_UP]:
        C['y'] -= velocidad_actual
    if T[pygame.K_s] or T[pygame.K_DOWN]:
        C['y'] += velocidad_actual
    if T[pygame.K_a] or T[pygame.K_LEFT]:
        C['x'] -= velocidad_actual
    if T[pygame.K_d] or T[pygame.K_RIGHT]:
        C['x'] += velocidad_actual
    if T[pygame.K_ESCAPE]:
        estado = "menu"

    C['x'] = max(C['radio'], min(C['x'], mapa_ancho - C['radio']))
    C['y'] = max(C['radio'], min(C['y'], mapa_alto - C['radio']))

    cam_x = C['x'] - AN // 2
    cam_y = C['y'] - AL // 2
    cam_x = max(0, min(cam_x, mapa_ancho - AN))
    cam_y = max(0, min(cam_y, mapa_alto - AL))

    P.blit(fondo, (-cam_x, -cam_y))
    pygame.draw.circle(P, (128, 0, 128), (int(C['x'] - cam_x), int(C['y'] - cam_y)), C['radio'])

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - inicio_juego_tiempo
    INTERVALO_CREACION = max(1000, 6000 - (tiempo_transcurrido // 10000) * 500)

    if len(ENEMIGOS) < MAX_ENEMIGOS and tiempo_actual - ULTIMA_CREACION >= INTERVALO_CREACION:
        crear_enemigo()
        ULTIMA_CREACION = tiempo_actual