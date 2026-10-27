import random


def calcular_dano_monstruo(player_atk, choice):
    match choice:
        case "attack":
            dano = player_atk
        case "magic":
            dano = player_atk * 2.5
        case _:
            dano = 0

    return dano


def apply_healing(player_hp):
    player_hp = player_hp + 30
    

    if player_hp > 100:
        player_hp = 100

    return player_hp


def check_battle_status(player_hp, monster_hp):
    if player_hp <= 0 and monster_hp <= 0:
        return "MUTUAL DEFEAT"
    elif monster_hp <= 0:
        return "VICTORY"
    elif player_hp <= 0:
        return "DEFEAT"
    else:
        return "Battle Continues"


def turn_resolution(player_hp, player_mana, player_atk, monster_hp, choice):
    monster_atk = random.randint(5, 25)

    match choice:
        case "attack":
            dano_monstruo = calcular_dano_monstruo(player_atk, choice)
            dano_jugador = monster_atk
            print("Atacaste al monstruo e hiciste", dano_monstruo, "de daño.")
            print("El monstruo te contraataca con", monster_atk, "y te hace", dano_jugador, "de daño.")

        case "magic":
            if player_mana >= 15:
                dano_monstruo = calcular_dano_monstruo(player_atk, choice)
                dano_jugador = monster_atk / 2
                player_mana = player_mana - 15
                print("Usaste magia e hiciste", dano_monstruo, "de daño.")
                print("El monstruo te contraataca con", monster_atk, "pero solo te hace", dano_jugador, "de daño (mitad).")
            else:
                print("No tienes suficiente mana. El hechizo falla.")
                dano_monstruo = 0
                dano_jugador = monster_atk
                print("El monstruo aprovecha y te contraataca con", monster_atk, "de daño completo.")

        case "heal":
            player_hp = apply_healing(player_hp)
            dano_monstruo = 0
            dano_jugador = monster_atk / 2
            print("Te curaste 30 de vida.")
            print("El monstruo te contraataca con", monster_atk, "pero solo te hace", dano_jugador, "de daño (mitad).")

        case _:
            print("Acción inválida. Pierdes el turno.")
            dano_monstruo = 0
            dano_jugador = monster_atk
            print("El monstruo te contraataca con", monster_atk, "de daño completo.")

    monster_hp = monster_hp - dano_monstruo
    player_hp = player_hp - dano_jugador

    if player_hp > 100:
        player_hp = 100
    if player_hp < 0:
        player_hp = 0
    if monster_hp < 0:
        monster_hp = 0

    estado = check_battle_status(player_hp, monster_hp)

    print()
    print("HP jugador:", player_hp, "| Mana:", player_mana, "| HP monstruo:", monster_hp)
    print("Estado:", estado)
    print()

    return player_hp, player_mana, monster_hp, estado


def main():
    nombre = input("Ingresa el nombre de tu jugador: ")
    print("Bienvenido, ", nombre)

    print()
    print("----- REGLAS DEL JUEGO -----")
    print("Tienes 3 acciones posibles: attack, magic, heal")
    print("- attack: le haces daño al monstruo igual a tu poder de ataque. El monstruo te contraataca completo.")
    print("- magic: cuesta 15 de mana. Le haces 2.5x tu poder de ataque. El monstruo te contraataca a la mitad.")
    print("         Si no tienes suficiente mana, el hechizo falla y el monstruo te pega completo.")
    print("- heal: recuperas 30 de vida (sin pasar de 100). El monstruo te contraataca a la mitad.")
    print()

    player_hp = 100

    player_mana = int(input("¿Cuánta mana quieres tener (0-50)? "))
    if player_mana > 50:
        player_mana = 50
    if player_mana < 0:
        player_mana = 0

    player_atk = int(input("¿Cuánto poder de ataque quieres (1-20)? "))
    if player_atk > 20:
        player_atk = 20
    if player_atk < 1:
        player_atk = 1

    monster_hp = 100

    estado = "Battle Continues"

    while estado == "Battle Continues":
        accion = input("Elige tu acción (attack/magic/heal): ")

        player_hp, player_mana, monster_hp, estado = turn_resolution(player_hp, player_mana, player_atk, monster_hp, accion)

    print()
    print("----- FIN DEL COMBATE -----")
    print("Resultado final:", estado)


main()