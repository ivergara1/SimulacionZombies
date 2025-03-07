# Simulación de Movimiento de Zombies

Este proyecto simula el movimiento de zombies en un edificio utilizando diferentes estrategias de movimiento. 

## Consideraciones Iniciales y Supuestos


- Para el diseño de los edificios se decide considerar construcciones con dimensiones X * m * n, con X = número de pisos, cada uno con una distribución rectangular de m filas y n columnas.
- Para el movimiento de los zombies, se decide que estos pueden trasladarse tanto a las habitaciones contiguas dentro del mismo piso, como a las habitaciones que se encuentran en la misma posición en los pisos de arriba y abajo de la habitación original.
- Se decide implementar dos estrategias diferentes; expansión y migración, las cuáles son detalladas más abajo. 

El proyecto está compuesto por los siguientes archivos:

- `estructura.py`
- `main.py`
- `simulacion.py`

## estructura.py

Este archivo define las clases `Sensor`, `Room` y `Building` que representan la estructura del edificio y las habitaciones.

- **Sensor**: Representa un sensor en una habitación que puede estar en estado "normal" o "alert".
- **Room**: Representa una habitación en el edificio que puede contener zombies y tiene un sensor.
  - Métodos:
    - `add_zombie(count=1)`: Añade una cantidad de zombies a la habitación y activa el sensor. Esta cantidad solamente toma importancia con la estrategia de movimiendo de migración, la cuál se explica más abajo.
    - `remove_zombies()`: Elimina todos los zombies de la habitación y resetea el sensor.
- **Building**: Representa el edificio con múltiples pisos y habitaciones.
  - Métodos:
    - `show_state()`: Muestra el estado actual del edificio.
    - `reset_building()`: Resetea el edificio eliminando todos los zombies y reseteando los sensores.

## simulacion.py

Este archivo define las estrategias de movimiento de los zombies y la clase `Simulation` que maneja la simulación.

- **ZombieMovementStrategy**: Clase base abstracta para las estrategias de movimiento de los zombies. Esta posee solamente un método: `move_zombies(building)`, el cuál varía en cada una de las siguientes subclases.
- **ExpansionStrategy**: Estrategia de expansión donde hay zombies "infinitos". Si una habitación se encuentra infectada, en cada turno se infectarán todas las habitaciones adyacentes.
- **MigrationStrategy**: Estrategia de migración donde los zombies son limitados. En cada turno cada zombie decide de manera aleatoria a qué habitación adyacente moverse. Si una habitación tiene uno o más zombies, el sensor se activará y aparecerá una letra "Z" a la hora de mostrar el estado.

- **Simulation**: Clase que maneja la simulación del movimiento de zombies en el edificio.
  - Métodos:
    - `advance_turn()`: Avanza un turno en la simulación moviendo los zombies.
    - `show_state()`: Muestra el estado actual de la simulación. Para cada habitación con zombies se mostrará una letra "Z", mientras que las habitaciones no infectadas están representadas por un guión "-".
    - `reset_building()`: Resetea el edificio y reinicia la simulación.
    - `to_dict()`: Convierte el estado actual de la simulación a un diccionario.
    - `from_dict(data)`: Restaura el estado de la simulación desde un diccionario.
    - `save_state(filename)`: Guarda el estado actual de la simulación en un archivo JSON.
    - `load_state(filename)`: Carga el estado de la simulación desde un archivo JSON.

## main.py

Este archivo contiene el punto de entrada principal del programa y maneja la interacción con el usuario.

- **Funciones**:
  - `validate_input(mensaje, min_value=0, max_value=None, constructor=False)`: Valida la entrada del usuario.
  - `main()`: Función principal que muestra el menú y maneja las opciones del usuario.

### **Comandos**:

#### Menú Principal
1. **Crear simulación**: Permite crear una nueva simulación ingresando el número de pisos, filas y columnas del edificio, y eligiendo la estrategia de movimiento de los zombies.
2. **Cargar simulación**: Permite cargar una simulación guardada desde un archivo JSON.
3. **Salir**: Sale del programa.

#### Menú de Simulación
1. **Mostrar estado**: Muestra el estado actual del edificio, indicando las habitaciones infectadas con una "Z" y las no infectadas con un "-".
2. **Avanzar turno**: Avanza un turno en la simulación, moviendo los zombies según la estrategia seleccionada.
3. **Añadir zombie**: Permite añadir zombies a una habitación específica ingresando el índice del piso, fila y columna. En la estrategia de migración, también se puede especificar la cantidad de zombies.
4. **Eliminar zombies de una habitación**: Elimina todos los zombies de una habitación específica ingresando el índice del piso, fila y columna.
5. **Reiniciar simulación**: Resetea el edificio eliminando todos los zombies y reseteando los sensores.
6. **Guardar simulación**: Guarda el estado actual de la simulación en un archivo JSON. Los estados se guardan en la carpeta "simulaciones".
7. **Volver al menú principal**: Regresa al menú principal.


### Uso

1. Clonar el repositorio:
```bash
git clone https://github.com/ivergara1/SimulacionZombies.git
```
2. Una vez en el directorio clonado ejecutar archivo `main.py`
```bash
python main.py
```
3. Seguir las instrucciones en el menú para crear una nueva simulación, cargar una simulación existente, mostrar el estado, avanzar turnos, añadir o eliminar zombies, reiniciar o guardar la simulación.
