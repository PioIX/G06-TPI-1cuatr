# Actividad 1 - Proyecto de Producción
Fornés, Mennuti, Santa Cruz, Tartaglia - 5to A Infomática

Bienvenidos!
Para jugar a nuestro Wordle necesitaras tener en cuenta un par de cosas: 
- Ambos archivos deben estar en una misma carpeta.
- Todas las palabras están en minúscula y no incluyen tildes.
- Dependiendo el nivel de dificultad que elijas al empezar el juego, el largo de las palabras va a cambiar ("Dificultad 1", son palabras de 4 letras con infinitos intentos, "Dificultad 2" van a ser de 5 letras y 7 intentos, y "Dificultad 3" van a ser de 6 letras y 5 intentos.) 

Antes de correr el código, tendrás que cambiar la dirección del archivo dependiendo de dónde lo hayas guardado: f = open(r"C:**\Users\alumno\Desktop**\palabras.txt", "r") La parte resaltada en negrita es lo que hay que cambiar según la ubicación del archivo.

Una vez ingreses una palabra, el programa te va a indicar 3 cosas: Si la letra está en la palabra y en la posición correcta, debajo aparecerá un "=". Si la letra está en la palabra pero no en la posición correcta, debajo aparecerá un "-". Si la letra no está dentro de la palabra, debajo estará vacío. 
