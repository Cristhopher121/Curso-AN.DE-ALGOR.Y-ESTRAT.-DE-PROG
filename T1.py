"Problema 1"
import random
 
 
def crearEntrenador(tupla):
    nombre_entrenador = input("Ingrese el nombre del entrenador: ")
    nombre_pokemon = input("Ingrese el nombre del pokemon: ")
    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)
    tupla.append((nombre_entrenador, nombre_pokemon, ataque, vida))
    print(f"\nEntrenador {nombre_entrenador} con pokemon {nombre_pokemon} "
          f"creado (Ataque={ataque}, Vida={vida}).\n")
 
 
def ordenBurbuja(lis):
    for i in range(1, len(lis)):
        for j in range(len(lis) - 1):
            if lis[j][2] < lis[j + 1][2]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis
 
 
def listaEntrenador(tupla):
    lista = ordenBurbuja(list(tupla))
 
    print("\n--- Lista de Entrenadores (ordenada por ataque) ---")
    if not lista:
        print("No hay entrenadores registrados.")
    else:
        print(f"{'#':<4}{'Entrenador':<15}{'Pokemon':<15}{'Ataque':<10}{'Vida':<10}")
        for idx, (entrenador, pokemon, ataque, vida) in enumerate(lista, start=1):
            print(f"{idx:<4}{entrenador:<15}{pokemon:<15}{ataque:<10}{vida:<10}")
    print("-----------------------------------------------------\n")
    return lista
 
 
def ordenSeleccion(lista):
    n = len(lista)
    for manoIzq in range(n):
        ind_min_val = manoIzq
        for vista in range(manoIzq + 1, n):
            if lista[vista][3] < lista[ind_min_val][3]:
                ind_min_val = vista
 
        lista[manoIzq], lista[ind_min_val] = lista[ind_min_val], lista[manoIzq]
    return lista
 
 
def busqueda_binaria(array, numero):
    menor = 0
    mayor = len(array) - 1
    for data in range(len(array)):
        medio = (menor + mayor) // 2
        if array[medio][3] == numero:
            return medio
        elif array[medio][3] < numero:
            menor = medio
        else:
            mayor = medio
        if mayor - menor <= 1:
            break
    if array[menor][3] == numero:
        return menor
    elif array[mayor][3] == numero:
        return mayor
    return -1
 
 
def borraPorPokemon(tupla):
    if not tupla:
        print("\nNo hay pokemones para borrar.\n")
        return
 
    try:
        vida_buscada = int(input("Ingrese el valor de vida a buscar: "))
    except ValueError:
        print("Valor invalido.\n")
        return
 
    ordenada = ordenSeleccion(list(tupla))
    pos = busqueda_binaria(ordenada, vida_buscada)
 
    if pos == -1:
        print(f"\nNo se encontro ningun pokemon con vida = {vida_buscada}.\n")
        return
 
    encontrado = ordenada[pos]
    tupla.remove(encontrado)
    print(f"\nSe elimino a {encontrado[0]} y su pokemon {encontrado[1]} "
          f"(Vida={encontrado[3]}).\n")
 
 
def peleaPokemon(lista):
    if len(lista) < 2:
        print("\nSe necesitan al menos 2 pokemones para pelear.\n")
        return
 
    ordenada = listaEntrenador(lista)
 
    try:
        n1 = int(input("Ingrese el numero del primer pokemon: "))
        n2 = int(input("Ingrese el numero del segundo pokemon: "))
    except ValueError:
        print("Valor invalido.\n")
        return
 
    if n1 == n2 or not (1 <= n1 <= len(ordenada)) or not (1 <= n2 <= len(ordenada)):
        print("Seleccion invalida.\n")
        return
 
    p1 = ordenada[n1 - 1]
    p2 = ordenada[n2 - 1]
 
    golpe1 = p1[2] * random.randint(0, 5)
    golpe2 = p2[2] * random.randint(0, 5)
 
    vida1_final = p1[3] - golpe2
    vida2_final = p2[3] - golpe1
 
    print(f"\n{p1[1]} (de {p1[0]}) ataca con {golpe1} de daño.")
    print(f"{p2[1]} (de {p2[0]}) ataca con {golpe2} de daño.")
    print(f"Vida restante de {p1[1]}: {vida1_final}")
    print(f"Vida restante de {p2[1]}: {vida2_final}\n")
 
    def eliminar_de_original(registro):
        if registro in lista:
            lista.remove(registro)
 
    if vida1_final <= 0 and vida2_final <= 0:
        print("¡Ambos pokemones quedaron sin vida! Ambos pierden y son eliminados.\n")
        eliminar_de_original(p1)
        eliminar_de_original(p2)
    elif vida1_final == vida2_final:
        print("¡Empate! Ambos pokemones pierden y son eliminados.\n")
        eliminar_de_original(p1)
        eliminar_de_original(p2)
    elif vida1_final > vida2_final:
        print(f"¡Gana {p1[0]} con su pokemon {p1[1]}!\n")
        eliminar_de_original(p2)
    else:
        print(f"¡Gana {p2[0]} con su pokemon {p2[1]}!\n")
        eliminar_de_original(p1)
 
 
def menu():
    entrenadores = []
 
    while True:
        print("===== MENU POKEMON =====")
        print("1. Crear Entrenador")
        print("2. Listar Entrenadores")
        print("3. Borrar por Pokemon")
        print("4. Pelea Pokemon")
        print("5. Fin")
        opcion = input("Elija una opcion: ")
 
        if opcion == "1":
            crearEntrenador(entrenadores)
        elif opcion == "2":
            listaEntrenador(entrenadores)
        elif opcion == "3":
            borraPorPokemon(entrenadores)
        elif opcion == "4":
            peleaPokemon(entrenadores)
        elif opcion == "5":
            print("Fin del juego. ¡Hasta luego!")
            break
        else:
            print("Opcion invalida, intente de nuevo.\n")
 
 
if __name__ == "__main__":
    menu()
