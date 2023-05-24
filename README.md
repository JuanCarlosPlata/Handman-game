# Hangman Game

## Descripción

El programa es un juego del ahorcado (Hangman Game) implementado en Python utilizando la biblioteca Tkinter para la interfaz gráfica. El propósito del programa es permitir que el jugador adivine una palabra oculta seleccionada al azar y evitar que se agoten todas las vidas.

## Funcionamiento

El juego presenta una interfaz gráfica donde se muestra una imagen del ahorcado y una palabra oculta representada por guiones bajos. El jugador debe ingresar letras para intentar adivinar la palabra. Si la letra ingresada está presente en la palabra oculta, se revela en la posición correcta. Si la letra no está presente, se muestra una parte adicional de la imagen del ahorcado. El jugador tiene un número limitado de vidas antes de perder el juego.

El juego continúa hasta que el jugador adivina todas las letras de la palabra oculta o se agotan todas las vidas. Después de cada ronda exitosa, el jugador avanza a una nueva palabra oculta.

El programa también guarda las mejores puntuaciones en un archivo de texto, donde se registran los nombres de los jugadores y el número de rondas completadas.

## Requisitos

El programa requiere tener instalados los siguientes elementos:

- Python 3.x
- La biblioteca Tkinter
- La biblioteca PIL (Pillow)

## Instrucciones de Uso

1. Ejecuta el archivo `hangman_game.py` con Python.
2. Se abrirá una ventana con la interfaz del juego.
3. Ingresa tu nombre en el cuadro de diálogo que aparece.
4. Adivina letras para completar la palabra oculta antes de que se agoten todas las vidas.
5. Después de cada ronda exitosa, se mostrará un mensaje y se avanzará a una nueva palabra oculta.
6. Al finalizar el juego, se mostrará tu puntuación y podrás ver las mejores puntuaciones registradas.

¡Diviértete jugando al ahorcado!
