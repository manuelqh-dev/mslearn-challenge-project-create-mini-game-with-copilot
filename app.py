import random

def check_value_in_list(value, opciones):
    return value in opciones

def repeat_fight():
    repeat = input("¿Deseas repetir la pelea? (s/n): ")
    if repeat.lower() == "s":
        chosen_value = input("Selecciona un valor de la lista: ")
        print("Has elegido:", chosen_value)

        while not check_value_in_list(chosen_value, opciones):
            chosen_value = input("Introduce un valor correcto: ")
            print("Has elegido:", chosen_value)

        print("Correcto.")
        random_value = random.choice(opciones)
        fight(chosen_value, random_value)
        repeat_fight()  # Recursive call to repeat the fight
    else:
        print("Fin del juego.Tu puntuación es:", counter)

opciones = ["piedra", "papel", "tijera"]
random_value = random.choice(opciones)
print("Opciones:", opciones)

chosen_value = input("Selecciona un valor de la lista: ")
print("Has elegido:", chosen_value)

while not check_value_in_list(chosen_value, opciones):
    chosen_value = input("Introduce un valor correcto: ")
    print("Has elegido:", chosen_value)

print("Correcto.")


counter = 0

def fight(chosen_value, random_value):
    global counter

    if chosen_value == random_value:
        print("Empate")
    elif chosen_value == "piedra" and random_value == "papel":
        print("Pierdes, Gana papel")
    elif chosen_value == "papel" and random_value == "tijera":
        print("Pierdes, Gana tijera")
    elif chosen_value == "tijera" and random_value == "piedra":
        print("Pierdes, Gana piedra")
    else:
        counter += 1
        print("Ganaste", chosen_value)

        
fight(chosen_value, random_value)
repeat_fight()





    
