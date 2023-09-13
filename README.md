# EmolgApp

# Notas:
- Ver como puedo plotear los botones y demas con un `zorder`.
- Hacer una forma de guardado de la escena, y carga. Ver cual es la mejor forma, quizás en `tmp`.

### Objetivo
- Crear una app full python para el streaming de Rodri [@terremotoparatodos](https://www.twitch.tv/terremotoparatodos)

### Pipeline (brainstorm)
1. Arquitectura base de pygame.
    1. Objeto escena.
        - Elementos que lo compone.
        - Widgets.
        - Como interactúan éstos con los diferentes módulos del software.
        - Puede haber un gestor de widgets que se encargue de hacer las peticiones.
        - Y todos deberían heredar de una clase base que es la que tiene la lógica para mandar peticiones.
    2. Objeto multimedia o similar. Que tenga las rutas y forma de acceder a los paths de archivos en el sistema.
    3. Me imagino que los widgets y demás necesitan cargar en memoria la imagen.
    4. 
