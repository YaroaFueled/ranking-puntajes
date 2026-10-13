# Ranking de Puntajes de Videojuego
# Autor: Samir Bueno
# Proyecto: Capítulo IX - Arreglos y Vectores (Introducción a la Programación)

# Dos vectores paralelos: la posición i de uno corresponde a la posición i del otro
jugadores = ["Yaroa", "Ana", "Luis", "Marta", "Pedro", "Sofía"]
puntajes = [1200, 850, 2300, 1560, 640, 1000]

PUNTAJE_CLASIFICACION = 1000


def mostrar_ranking():
    print("\n--- PUNTAJES ACTUALES ---")
    for i in range(len(jugadores)):
        print(f"[{i}] {jugadores[i]}: {puntajes[i]} puntos")


def consultar_por_indice():
    pos = int(input("Ingrese la posición (índice) del jugador: "))
    if 0 <= pos < len(jugadores):
        print(f"El jugador en la posición {pos} es {jugadores[pos]} con {puntajes[pos]} puntos.")
    else:
        print(f"Esa posición no existe. Use un número entre 0 y {len(jugadores) - 1}.")


def estadisticas():
    promedio = sum(puntajes) / len(puntajes)
    mayor = puntajes[0]
    menor = puntajes[0]
    pos_mayor = 0
    pos_menor = 0
    for i in range(len(puntajes)):
        if puntajes[i] > mayor:
            mayor = puntajes[i]
            pos_mayor = i
        if puntajes[i] < menor:
            menor = puntajes[i]
            pos_menor = i
    print("\n--- ESTADÍSTICAS ---")
    print(f"Promedio de puntos: {promedio:.2f}")
    print(f"Mejor puntaje: {jugadores[pos_mayor]} con {mayor} puntos")
    print(f"Menor puntaje: {jugadores[pos_menor]} con {menor} puntos")


def contar_clasificados():
    clasificados = 0
    for puntaje in puntajes:
        if puntaje >= PUNTAJE_CLASIFICACION:
            clasificados += 1
    no_clasificados = len(puntajes) - clasificados
    print(f"\nClasificados (>= {PUNTAJE_CLASIFICACION} puntos): {clasificados}")
    print(f"No clasificados: {no_clasificados}")


def modificar_puntaje():
    pos = int(input("Posición del jugador a modificar: "))
    if 0 <= pos < len(puntajes):
        viejo = puntajes[pos]
        nuevo = int(input(f"Nuevo puntaje para {jugadores[pos]} (actual {viejo}): "))
        puntajes[pos] = nuevo
        print(f"Puntaje de {jugadores[pos]} cambiado de {viejo} a {nuevo}.")
    else:
        print("Esa posición no existe.")


def buscar_jugador():
    nombre = input("Nombre del jugador a buscar: ").strip()
    encontrado = False
    for i in range(len(jugadores)):
        if jugadores[i].lower() == nombre.lower():
            print(f"{jugadores[i]} está en la posición {i} con {puntajes[i]} puntos.")
            encontrado = True
    if not encontrado:
        print("Jugador no encontrado.")


def menu():
    opcion = ""
    while opcion != "0":
        print("\n===== RANKING DE PUNTAJES =====")
        print("1. Mostrar puntajes")
        print("2. Consultar jugador por posición")
        print("3. Ver estadísticas")
        print("4. Contar clasificados")
        print("5. Modificar un puntaje")
        print("6. Buscar jugador por nombre")
        print("0. Salir")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            mostrar_ranking()
        elif opcion == "2":
            consultar_por_indice()
        elif opcion == "3":
            estadisticas()
        elif opcion == "4":
            contar_clasificados()
        elif opcion == "5":
            modificar_puntaje()
            mostrar_ranking()
        elif opcion == "6":
            buscar_jugador()
        elif opcion == "0":
            print("¡Hasta luego!")
        else:
            print("Opción no válida.")


menu()
