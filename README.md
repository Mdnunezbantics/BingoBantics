# BingoBantics
Antes de usar el programa recordar instalar los requerimentos en 
requeriments.txt

El programa genera cartones cumnpliendo los siguientes requisitos:
* cada carton es distinto de los otros generados
* cada fila tiene 5 numeros
* cada carton tiene 15 numeros en total
* cada 6 cartones generados en una hoja estan los numeros del 1 al 90

El programa genera hojas de 12 cartones cada una y cada hoja tiene un 
numero de tira unico en la tanda de generacion, a su ves si se realiza el 
trabajo completo se generan las tiras "testigo" que cunmplen la funcion de 
duplicado del original para su verificacion.

Se adiciona la generacion de un archivo pickle para guardar los numeros de
los cartones permitiendo guardar el trabajo ocupando muy poco espacio

Se hisieron pruebas generando 60000 cartones donde se cumplieron todos los 
requisitos antes mencionados

Ejecutando el archivo main como primer paso nos ira haciendo una serie
de consultas para generar el trabajo solicitado, como primer paso
nos pregunta si se genera la lista de numeros nueva o usaremos una que 
ya tenemos generada, siempre estos archivos deben estar en una carpeta especifica 
llamada Pickle por defecto y el nombre que se empleara por default estara
comprendido por la fecha actual + el nombre de cliente

Como paso dos se procede a realizar el trabajo completo para asegurar 
la igualdad de los cartones primero armaremos una base de ellos como png
que luego emplearemos para generar los llamados "originales" y "testigos"
la salida final del trabajo sera en formato de pdf y podremos indicar la 
cantidad de hojas que tendra cada uno, el formato que usamos es de 
oficio (22x34 mm) cortandolo a la mitad como ya hemos dicho cada hoja
se compone de 2 tiras distintas

Si ya tenemos los png antes mencionados no nesesitamos realizar el trabajo
completo ahorrando mucho tiempo
