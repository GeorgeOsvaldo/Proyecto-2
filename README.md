 Descripción del Proyecto

Este programa consta de dos problemas o ejercicios resueltos en Python que interactúan con el usuario a través de la consola.

## Problema 1: Validación de palabra

- Solicita al usuario que ingrese una palabra que tenga entre 4 y 8 letras.
- Verifica que la palabra contenga **solo letras** (sin números, espacios ni símbolos).
- Comprueba que la longitud de la palabra esté dentro del rango especificado (4 a 8 caracteres).
- Si alguna de estas condiciones no se cumple, muestra un mensaje de error y vuelve a pedir la palabra.
- Si la palabra es válida, muestra un mensaje de confirmación y termina esta parte.

## Problema 2: Determinar el cuadrante de un punto

- Solicita al usuario que ingrese dos valores numéricos, que representan las coordenadas X y Y de un punto en el plano cartesiano.
- Valida que ambos valores sean números (permitiendo números decimales).
- Determina en qué cuadrante se encuentra el punto según las coordenadas ingresadas:
  - Primer cuadrante: X > 0, Y > 0
  - Segundo cuadrante: X < 0, Y > 0
  - Tercer cuadrante: X < 0, Y < 0
  - Cuarto cuadrante: X > 0, Y < 0
  - Si el punto está sobre alguno de los ejes X o Y, vuelve a pedir los valores.
- Finalmente, muestra el resultado y termina la ejecución.
