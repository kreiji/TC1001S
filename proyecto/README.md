<h1>Proyecto TC1001S</h1>

<h2>Equipo</h2>
María Carelia Ibarra Vásquez A01251463
Jesús Francisco Fong Ruíz A01254062
Santiago Ramírez Enríquez A01254173

<h2>Materia y Fecha</h2>
Herramientas Computacionales: El Arte de la Programacion (Semana Tec) TC1001S.201
13 de mayo del 2022

<h2>Explicacion del Codigo</h2>
El codigo de "simonsays.py" fue conseguido desde la página de Free Python Games (https://grantjenks.com/docs/freegames/simonsays.html). El código base dibuja cuatro cuadros de colores diferentes y espera hasta que el jugador de click para comenzar el juego. El código elige cuadros al azar para crear un patrón, y cuando se elijen los cuadros cambian a un tono más brillante para mostrar que ese cuadro es el siguiente en el patrón. Finalmente el jugador debe repetir el patrón hecho por el código, y el programa verifica que el usuario haya seguido el mismo orden; en el caso de haberlo hecho se agrega un cuadro más al patrón, de lo contrario el juego termina y la ventana se cierra.


Hicimos tres cambios (uno por cada miembro del equipo). El primero es un contador que muestra el número de rondas, esto fue hecho escribiendo la longitud del patrón. El segundo cambio fue darle al juego la habilidad de cambiar los colores de los cuadros aleatoriamente, esto fue hecho creando dos arreglos (uno para los colores oscuros y otro para los colores brillantes) despues se crearon variables con un valor aleatorio del 0 a 8 (equivalente a las longitudes de los arreglos que contienen los colores) y por último añadimos los colores en los vectores correspondientes a los cuadros (indicados por el índice de los arreglos). Finalmente, el último cambio fue agregar sonido, importamos la librería playsound, descargamos algunos sonidos (los cuales pusimos dentro de los vectores para los cuadros como strings) y cuando un cuadro se selecciona el sonido suena en el juego.

<h2>Video del Proyecto</h2>
https://youtu.be/6FUuptgwcSU
