nombres_epicos_geekdom = [
 ["Naofumi", "Filo", "Raphtalia"], 
 ["Rand Al'thor", "Perrin Arabaya", "Mathrim Cauldron", "Egwene Al'vere", "Nynaieve Al'mere"], 
 ["Lithany of Fury", "Macragge's Honour", "Vengeful Spirit", "Harbinger of Doom", "Chronicle of Ashes"],
 ["Cloud Strife", "Sephiroth", "Vincent Valentine", "Zack Fair", "Aerith Gainsborough", "Tifa Lockhart", "Barret Wallace", "Yuffie Kisaragi"],
 ["Cormyr", "WestGate", "Suzeil", "Menzoberranzan", "Waterdeep"],
 ["Atlas", "Dectective Comics", "Dark Horse", "Image"],
 ]

def crear_matriz(exterior: int, interior: int) -> list:
    matriz = []
    for _ in range(exterior):
        columna = []
        for _ in range(interior):
            data = int(input())
            columna.append(data)

        matriz.append(columna)

    return matriz

def suma_diagonal(matriz: list) -> int:
    suma = 0
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                suma += matriz[i][j]

    return suma

def suma_diagonal_inversa(matriz):
    suma = 0
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False
        
    for i in range(len(matriz)):
        suma += matriz[i][n - i - 1]

    return suma

def encuentra_grupo(nombres_epicos: list, nombre: str):
    for grupo in nombres_epicos:
        if nombre in grupo:
            return grupo

    return "el nombre no es epico"


def main():
    opcion = int(input())
    if opcion == 1:
        exterior = int(input())
        interior = int(input())
        print(crear_matriz(exterior, interior))

    elif opcion == 2:
        exterior = int(input())
        interior = int(input())
        matriz = crear_matriz(exterior, interior)
        print(suma_diagonal(matriz))

    elif opcion == 3:
        exterior = int(input())
        interior = int(input())
        matriz = crear_matriz(exterior, interior)
        print(suma_diagonal_inversa(matriz))

    elif opcion == 4:
        nombre = input()
        print(encuentra_grupo(nombres_epicos_geekdom, nombre))

    else:
        print("entrada no valida")

if __name__ == "__main__":
    main()