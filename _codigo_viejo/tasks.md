# Tareas
    1. Crear menu de inicio, con la selección de la resolucion de pantalla.
       1. Selección de la resolución. (Guardar la primer elección que haga para futuros ingresos a la app)
    2. 

# Recordatorios
### Botones
- Agregar memoria "caché" a los botones, me imagino algo tipo:
    ~~~python
    self._cache = {}        # Y acá se podrían guardar diferentes datos.
    self._cache = value     # Para botones que no necesiten más de un valor.
    ~~~
    Me imagino, por ejemplo, para los check buttons solo necesitan un booleano. Las listas desplegables necesitan varios, uno por cada valor y tener que conectarlos de alguna manera.
- Ver como agregarle typing a btn en la clase wrappers de los botones. (circular import)
- Agregar una funcionalidad para que lea un yaml y no tener que hard-00codear los parámetros de los botones.

### Escena
- Agregar un "telón" para el cambio de escena, así todo el procesamiento que se tiene que hacer cuando se cambia de escena el usuario no lo nota.







