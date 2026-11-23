"""
contador_poo.py
===============
Contador interactivo con Pygame aplicando Programación Orientada a Objetos.

Clases:
    - Boton: encapsula geometría, colores, texto, detección de hover/clic
      y su propio método de dibujado.
    - AplicacionContador: administra la ventana, el estado del contador,
      los botones, el manejo de eventos y el ciclo principal.

Ejecución:
    python contador_poo.py
"""

import sys

import pygame


class Boton:
    """Botón rectangular interactivo con efecto hover."""

    def __init__(self, x, y, ancho, alto, texto, color_normal, color_hover,
                 fuente, color_texto=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.color_texto = color_texto
        self.fuente = fuente

    def esta_sobre(self, posicion):
        """Indica si el cursor (x, y) está dentro del botón."""
        return self.rect.collidepoint(posicion)

    def fue_clicado(self, evento):
        """
        Valida que el evento sea un clic izquierdo (MOUSEBUTTONDOWN,
        button == 1) realizado dentro del área del botón.
        """
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
            and self.esta_sobre(evento.pos)
        )

    def dibujar(self, superficie):
        """Dibuja el botón; el color depende de si el cursor está encima."""
        color = self.color_hover if self.esta_sobre(pygame.mouse.get_pos()) \
            else self.color_normal

        pygame.draw.rect(superficie, color, self.rect, border_radius=12)
        pygame.draw.rect(superficie, self.color_texto, self.rect,
                         width=2, border_radius=12)

        superficie_texto = self.fuente.render(self.texto, True, self.color_texto)
        rect_texto = superficie_texto.get_rect(center=self.rect.center)
        superficie.blit(superficie_texto, rect_texto)


class AplicacionContador:
    """Aplicación principal: ventana, estado, botones y Game Loop."""

    ANCHO = 480
    ALTO = 360
    FPS = 60
    TITULO = "Contador Interactivo - Versión POO (Pygame)"

    COLOR_FONDO = (30, 30, 46)
    COLOR_TEXTO = (240, 240, 240)

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption(self.TITULO)
        self.reloj = pygame.time.Clock()

        # Fuentes del sistema (sin archivos externos)
        self.fuente_titulo = pygame.font.SysFont("arial", 26)
        self.fuente_contador = pygame.font.SysFont("arial", 96, bold=True)
        self.fuente_boton = pygame.font.SysFont("arial", 22)

        # Estado de la aplicación
        self.contador = 0
        self.ejecutando = True

        # Botones: Incrementar (azul) y Reiniciar (rojo)
        ancho_boton, alto_boton, separacion = 190, 55, 20
        x_inicial = (self.ANCHO - (2 * ancho_boton + separacion)) // 2
        y_botones = 265

        self.boton_incrementar = Boton(
            x_inicial, y_botones, ancho_boton, alto_boton,
            "Incrementar +1", (66, 135, 245), (110, 170, 255),
            self.fuente_boton,
        )
        self.boton_reiniciar = Boton(
            x_inicial + ancho_boton + separacion, y_botones,
            ancho_boton, alto_boton,
            "Reiniciar a 0", (220, 70, 80), (250, 110, 120),
            self.fuente_boton,
        )
        self.botones = [self.boton_incrementar, self.boton_reiniciar]

    # ------------------------------------------------------------------
    # Lógica de eventos
    # ------------------------------------------------------------------
    def manejar_eventos(self):
        """Procesa la cola de eventos de Pygame."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif self.boton_incrementar.fue_clicado(evento):
                self.contador += 1
            elif self.boton_reiniciar.fue_clicado(evento):
                self.contador = 0

    # ------------------------------------------------------------------
    # Renderizado
    # ------------------------------------------------------------------
    def _dibujar_texto(self, texto, fuente, centro):
        superficie = fuente.render(texto, True, self.COLOR_TEXTO)
        self.pantalla.blit(superficie, superficie.get_rect(center=centro))

    def dibujar(self):
        """Dibuja todos los elementos y actualiza la pantalla."""
        self.pantalla.fill(self.COLOR_FONDO)
        self._dibujar_texto("Contador", self.fuente_titulo, (self.ANCHO // 2, 45))
        self._dibujar_texto(str(self.contador), self.fuente_contador,
                            (self.ANCHO // 2, 150))
        for boton in self.botones:
            boton.dibujar(self.pantalla)
        pygame.display.flip()

    # ------------------------------------------------------------------
    # Ciclo principal
    # ------------------------------------------------------------------
    def ejecutar(self):
        """Game Loop: eventos -> dibujado -> control de FPS."""
        while self.ejecutando:
            self.manejar_eventos()
            self.dibujar()
            self.reloj.tick(self.FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    AplicacionContador().ejecutar()
