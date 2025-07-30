#####################################################################################
#######################################Problema 1####################################
#####################################################################################
while True:
    # Pedimos al usuario que ingrese una palabra
    palabra = input("Ingresa una palabra que tenga entre 4 y 8 letras:  ")

    # Comprobamos si la palabra contiene solo letras (sin números, símbolos ni espacios)
    if not palabra.isalpha():
        # Si contiene algo que no sea letra, mostramos un mensaje de error
        print("La palabra solo debe contener letras (sin números, espacios ni símbolos).")

    # Si contiene menos de 4 letras, mostramos el mensaje
    elif len(palabra) < 4:
        print(f"La palabra tiene menos de 4 letras. Contiene {len(palabra)} letra(s).")

    # Si contiene más de 8 letras, mostramos el mensaje
    elif len(palabra) > 8:
        print(f"La palabra tiene más de 8 letras. Contiene {len(palabra)} letra(s).")

    # Si todo es correcto, salimos del bucle
    else:
        print("La palabra es correcta.")
        break# Como cumplió el objetivo, rompemos el bucle

#####################################################################################
######################################Problema 2#####################################
#####################################################################################

while True:
    posicion_x = input("Ingrese la posición X: ")
    posicion_y = input("Ingrese la posición Y: ")
    # Verificamos si las posiciones son números
    if not (posicion_x.replace('.', '', 1).isdigit() and posicion_y.replace('.', '', 1).isdigit()):
        print("Las posiciones deben ser números.")
        continue  # Si no son números, volvemos a pedir las posiciones
    else:
        posicion_x = float(posicion_x)
        posicion_y = float(posicion_y)

        # Verificamos en qué cuadrante se encuentra el punto
        if posicion_x > 0 and posicion_y > 0:
            print("El punto está en el primer cuadrante.")
        elif posicion_x < 0 and posicion_y > 0:
            print("El punto está en el segundo cuadrante.")
        elif posicion_x < 0 and posicion_y < 0:
            print("El punto está en el tercer cuadrante.")
        elif posicion_x > 0 and posicion_y < 0:
            print("El punto está en el cuarto cuadrante.")
        else:
            print("El punto está sobre uno de los ejes.")   
        break
