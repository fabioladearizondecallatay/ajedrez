He querido hacer un juego de ajedrez donde 
- se pueden mover las piezas
- los movimientos se guardan en un nuevo fichero con el nombre que los jugadores desean darle a la partida
- se guardan tambien el tablero inicial y el tablero modificado tras cada movimiento (que esta numerotado)
- se puede al final de la partida preguntar de ver el tablero en el movimiento x

Para eso, primero he creado una classe llamada chess donde he definido todas las funciones que crean el juego.
Las funciones son : 
- __init__ : para para definir el jugador, su tablero y sus movimientos (guardados en una lista)
- init_board : para configurar el tablero inicial con los dibujos de las piezas
- save_game : para guardar el estado inicial del tablero en el fichero de la partida (llamado ..._ajedrez.txt)
- show_board : para hacer el tablero mas visual y poder usarlo para hacer los movimientos
- move_piece : para mover las piezas y quitar los posibles errores
- save_move : para guardar el movimiento hecho en el fichero y el tablero modificado con su numero asignado
- consult_move : para proponer a los jugadores al finalde la partida de revisitar algun movimiento
- convert_notacion : para que los movimientos guardados sean con la misma anotacion que lo que esta alrededor del tablero

Luego fuera de la clase chess he definido la funcion principal del juego que es play_chess donde defino variables y hago el bucle del desarollo de juego. 

Termino con if __name__ == "__main__": para marcar que play_chess es la funcion principal y que se define como el script principal.
