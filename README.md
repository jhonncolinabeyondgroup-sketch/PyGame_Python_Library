# 🎮 Contador Interactivo con Pygame

Proyecto académico que presenta la biblioteca **Pygame** mediante una aplicación sencilla: un **contador interactivo** con botones, implementado de dos formas (estructurada y orientada a objetos).

**Pygame** es un conjunto de módulos de Python, de código abierto y multiplataforma, diseñado para crear videojuegos y aplicaciones multimedia. Está construido sobre la biblioteca **SDL** (Simple DirectMedia Layer), que le da acceso a gráficos 2D, sonido, teclado, ratón y *joysticks*.

---

## 📚 Investigación técnica sobre Pygame

### ¿Cuál es su propósito principal?

Proporcionar a los programadores de Python una forma sencilla de crear **videojuegos y programas multimedia interactivos**. Abstrae las tareas de bajo nivel (ventanas, dibujo, entrada de usuario, audio y temporización) para que el desarrollador se concentre en la lógica de su aplicación.

### ¿Qué tipo de aplicaciones permite desarrollar?

- Videojuegos 2D (plataformas, *arcade*, puzzles, juegos de mesa).
- Prototipos de juegos y *game jams*.
- Simulaciones y visualizaciones interactivas (física, autómatas, algoritmos).
- Aplicaciones educativas e interactivas con interfaz gráfica personalizada.
- Herramientas multimedia sencillas (reproductores, editores de sprites o mapas).

### ¿Cómo se instala y qué requisitos necesita?

**Requisitos:** Python 3 (se recomienda 3.8 o superior) y `pip`. Pygame distribuye *wheels* precompilados para Windows, macOS y Linux, por lo que normalmente no requiere compilar nada.

```bash
pip install pygame
# o, para este proyecto:
pip install -r requirements.txt
```

Para verificar la instalación:

```bash
python -m pygame.examples.aliens
```

### ¿Cuáles son sus principales componentes o elementos gráficos?

| Módulo / Clase | Descripción |
|---|---|
| `pygame.display` | Crea y gestiona la ventana (`set_mode`, `set_caption`, `flip`, `update`). |
| `pygame.Surface` | Objeto que representa una imagen o superficie de dibujo. La pantalla principal es una `Surface`; sobre ella se hace `blit` de otras superficies. |
| `pygame.Rect` | Rectángulo con posición y tamaño. Facilita colisiones (`collidepoint`, `colliderect`), centrado y movimiento. |
| `pygame.draw` | Primitivas gráficas: `rect`, `circle`, `line`, `polygon`, `ellipse`, etc. |
| `pygame.font` | Renderizado de texto (`SysFont`, `Font`, `render`) que produce una `Surface`. |
| `pygame.sprite` | Clases `Sprite` y `Group` para gestionar objetos de juego, dibujarlos en bloque y detectar colisiones. |
| `pygame.time` | `Clock` para controlar los FPS (`tick`) y temporizadores (`get_ticks`, `set_timer`). |

### ¿Cómo maneja los eventos del usuario?

Pygame utiliza una **cola de eventos**: cada acción del usuario (mover el ratón, pulsar una tecla, cerrar la ventana) se convierte en un objeto `pygame.event.Event` que se almacena en una cola. Con `pygame.event.get()` el programa extrae todos los eventos pendientes y los procesa uno a uno dentro del bucle principal.

| Evento | Cuándo se genera | Atributos útiles |
|---|---|---|
| `QUIT` | El usuario cierra la ventana. | — |
| `MOUSEBUTTONDOWN` | Se presiona un botón del ratón. | `pos`, `button` (1 = izquierdo, 2 = central, 3 = derecho) |
| `KEYDOWN` | Se presiona una tecla. | `key`, `unicode`, `mod` |

```python
for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        ejecutando = False
    elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        print("Clic izquierdo en", evento.pos)
    elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
        print("Se presionó la barra espaciadora")
```

### Ventajas y limitaciones de Pygame frente a Tkinter

| Aspecto | Pygame | Tkinter |
|---|---|---|
| Propósito principal | Videojuegos y multimedia 2D | Aplicaciones de escritorio con formularios y widgets |
| Widgets predefinidos (botones, menús, cuadros de texto) | ❌ No incluye; hay que crearlos manualmente | ✅ Amplio conjunto listo para usar |
| Control gráfico y animación | ✅ Total, con renderizado por fotograma y 60+ FPS | ⚠️ Limitado (`Canvas` con `after`) |
| Sonido y música | ✅ Módulos `mixer` y `music` integrados | ❌ No incluye |
| Manejo de dispositivos (joystick, gamepad) | ✅ Soporte nativo | ❌ No disponible |
| Curva de aprendizaje para interfaces de formularios | ⚠️ Mayor esfuerzo | ✅ Muy rápida |
| Instalación | Requiere `pip install pygame` | ✅ Incluido con Python en la mayoría de distribuciones |
| Modelo de ejecución | Bucle principal escrito por el programador (*Game Loop*) | Bucle de eventos gestionado por `mainloop()` |
| Aspecto de la interfaz | ❌ Propio, no nativo | ✅ Más cercano al sistema operativo |

---

## ⚙️ Instalación y ejecución paso a paso

1. **Clonar el repositorio** (reemplaza `<tu-usuario>` por tu usuario de GitHub):

   ```bash
   git clone https://github.com/<tu-usuario>/pygame-contador-interactivo.git
   cd pygame-contador-interactivo
   ```

2. **(Opcional, recomendado) Crear un entorno virtual:**

   ```bash
   python -m venv venv
   # Linux / macOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la versión básica (estructurada):**

   ```bash
   python contador_basico.py
   ```

5. **Ejecutar la versión con Programación Orientada a Objetos:**

   ```bash
   python contador_poo.py
   ```

> En algunos sistemas el comando puede ser `python3` en lugar de `python`.

---

## 🧠 Explicación del ejemplo y funcionamiento de eventos

### El Game Loop

Toda aplicación Pygame gira en torno a un **bucle principal** que se repite 60 veces por segundo:

1. **Eventos:** se lee la cola con `pygame.event.get()`.
2. **Actualización:** se modifica el estado (en este caso, el valor del contador).
3. **Dibujado:** se limpia la pantalla (`fill`), se dibujan texto y botones, y se muestra el fotograma con `pygame.display.flip()`.
4. **Control de tiempo:** `Clock.tick(60)` limita la velocidad a 60 FPS.

### Detección de clics

Al producirse un `MOUSEBUTTONDOWN` con `button == 1` (clic izquierdo), se toma la posición del cursor (`evento.pos`) y se verifica con `Rect.collidepoint(pos)` si cae dentro del área del botón. Si es así, se incrementa el contador y en el siguiente fotograma se muestra el nuevo valor.

El **efecto hover** se logra consultando `pygame.mouse.get_pos()` en cada fotograma y eligiendo el color del botón según si el cursor está sobre su `Rect`.

### `contador_basico.py` (enfoque estructurado)

- Constantes globales para configuración y colores.
- Función `procesar_clic_boton()`: verifica la colisión y devuelve el contador actualizado.
- Funciones `dibujar_boton()` y `dibujar_texto_centrado()` para el renderizado.
- Función `main()` con el Game Loop.

### `contador_poo.py` (arquitectura orientada a objetos)

| Clase | Responsabilidades |
|---|---|
| **`Boton`** | Encapsula su `pygame.Rect`, el texto, los colores normal y hover y la fuente. Detecta si el cursor está encima (`esta_sobre`), valida un clic izquierdo dentro de su área (`fue_clicado`) y se dibuja a sí mismo (`dibujar`). No conoce nada del contador: solo informa si fue presionado. |
| **`AplicacionContador`** | Inicializa Pygame y la ventana, mantiene el estado (`contador`), crea los botones *Incrementar +1* y *Reiniciar a 0*, procesa la cola de eventos (`manejar_eventos`), renderiza la escena (`dibujar`) y ejecuta el ciclo principal con control de FPS (`ejecutar`). |

Esta separación sigue el principio de **responsabilidad única**: el botón se ocupa de su interacción y apariencia, y la aplicación coordina el flujo general y decide qué ocurre cuando un botón es presionado.

---

## 🔗 Fuentes consultadas

- Documentación oficial de Pygame: <https://www.pygame.org/docs/>
- Sitio oficial de Pygame: <https://www.pygame.org>
- Guía de inicio (*Getting Started*): <https://www.pygame.org/wiki/GettingStarted>
- Referencia de `pygame.event`: <https://www.pygame.org/docs/ref/event.html>
- Referencia de `pygame.Rect`: <https://www.pygame.org/docs/ref/rect.html>
- Repositorio oficial en GitHub: <https://github.com/pygame/pygame>
- Documentación de Tkinter (Python): <https://docs.python.org/3/library/tkinter.html>
- SDL (Simple DirectMedia Layer): <https://www.libsdl.org>
