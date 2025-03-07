import concurrent.futures
import time

def tarea(nombre, duracion):
    """Simula una tarea que toma cierto tiempo en completarse."""
    time.sleep(duracion)
    return f"Tarea {nombre} completada en {duracion} segundos"

# Lista de tareas con sus duraciones
tareas = [("A", 3), ("B", 2), ("C", 1)]

# Usamos ThreadPoolExecutor para ejecutar las tareas en paralelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    futuros = {executor.submit(tarea, nombre, duracion): nombre for nombre, duracion in tareas}

    for futuro in concurrent.futures.as_completed(futuros):
        print(futuro.result())

print("¡Todas las tareas han finalizado!")
