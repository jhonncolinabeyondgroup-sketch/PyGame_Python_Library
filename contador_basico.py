
import sys

import pygame

# ---------------------------------------------------------------------------
# Constantes de configuración
# ---------------------------------------------------------------------------
ANCHO, ALTO = 480, 320
FPS = 60
TITULO = "Contador Interactivo - Versión básica (Pygame)"

# Colores en formato RGB
COLOR_FONDO = (30, 30, 46)
COLOR_TEXTO = (240, 240, 240)
COLOR_BOTON_NORMAL = (66, 135, 245)
COLOR_BOTON_HOVER = (110, 170, 255)
COLOR_TEXTO_BOTON = (255, 255, 255)

# Rectángulo del botón: (x, y, ancho, alto), centrado horizontalmente
RECT_BOTON = pygame.Rect(0, 0, 200, 60)
RECT_BOTON.center = (ANCHO // 2, 230)


# ---------------------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------------------
def procesar_clic_boton(posicion_mouse, rect_boton, contador):
    """
    Verifica si el clic ocurrió dentro del botón y, de ser así,
    incrementa el contador.

    Parámetros:
        posicion_mouse (tuple): coordenadas (x, y) del cursor al hacer clic.
        rect_boton (pygame.Rect): área rectangular del botón.
        contador (int): valor actual del contador.

    Retorna:
        int: nuevo valor del contador (incrementado si hubo colisión).
    """
    if rect_boton.collidepoint(posicion_mouse):
        contador += 1
    return contador


def dibujar_texto_centrado(pantalla, texto, fuente, color, centro):
    """Renderiza un texto y lo dibuja centrado en la posición indicada."""
    superficie_texto = fuente.render(texto, True, color)
    rect_texto = superficie_texto.get_rect(center=centro)
    pantalla.blit(superficie_texto, rect_texto)


def dibujar_boton(pantalla, rect_boton, fuente, posicion_mouse):
    """
    Dibuja el botón. Usa un color distinto si el cursor está encima (hover).
    """
    if rect_boton.collidepoint(posicion_mouse):
        color = COLOR_BOTON_HOVER
    else:
        color = COLOR_BOTON_NORMAL

    # Cuerpo del botón con esquinas redondeadas
    pygame.draw.rect(pantalla, color, rect_boton, border_radius=12)
    # Borde del botón
    pygame.draw.rect(pantalla, COLOR_TEXTO_BOTON, rect_boton, width=2, border_radius=12)
    # Texto del botón
    dibujar_texto_centrado(
        pantalla, "Incrementar +1", fuente, COLOR_TEXTO_BOTON, rect_boton.center
    )


# ---------------------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------------------
def main():
    # 1. Inicialización de Pygame y creación de la ventana
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(TITULO)
    reloj = pygame.time.Clock()

    # Fuentes del sistema (no requiere archivos .ttf externos)
    fuente_contador = pygame.font.SysFont("arial", 96, bold=True)
    fuente_boton = pygame.font.SysFont("arial", 24)
    fuente_titulo = pygame.font.SysFont("arial", 26)

    # 2. Estado de la aplicación
    contador = 0
    ejecutando = True

    # 3. Bucle principal (Game Loop)
    while ejecutando:
        # --- Posición actual del cursor (para el efecto hover) ---
        posicion_mouse = pygame.mouse.get_pos()

        # --- A. Manejo de eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # button == 1 corresponde al clic izquierdo
                contador = procesar_clic_boton(evento.pos, RECT_BOTON, contador)

        # --- B. Dibujado ---
        pantalla.fill(COLOR_FONDO)
        dibujar_texto_centrado(
            pantalla, "Contador", fuente_titulo, COLOR_TEXTO, (ANCHO // 2, 40)
        )
        dibujar_texto_centrado(
            pantalla, str(contador), fuente_contador, COLOR_TEXTO, (ANCHO // 2, 125)
        )
        dibujar_boton(pantalla, RECT_BOTON, fuente_boton, posicion_mouse)

        # --- C. Actualizar la pantalla ---
        pygame.display.flip()

        # --- D. Limitar la velocidad a 60 FPS ---
        reloj.tick(FPS)

    # 4. Cierre ordenado
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
