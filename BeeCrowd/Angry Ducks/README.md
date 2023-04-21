# Angry Ducks

## 1. comprensión del problema

---
A este ejercicio se le obtienen los siguientes datos importantes:

* La gravedad ( $g$ ) y $pi$ estan previamente suministrados por el problema.
* Calcular si teniendo la altura del tirachinas $h$, los puntos donde *Nlogony City*
que empieza ( $p_{1}$ ) y acaba ( $p_{2}$ ), el ángulo de tiro ( $\alpha$ ) y la velocidad
de disparo ( $v$ ), dará en el blanco.
* $1\leqslant h \leqslant 150$ siendo un valor con coma flotante (float) y la primera linea
de entrada de datos.
* $1\leqslant p_{1},p_{2} \leqslant 9999$ siendo un valor entero (int) y la segunda entrada
de datos.
* $1\leqslant n \leqslant 100$ el número de intentos.
* Las $n$ lineas siguientes contienen dos valores tipo float indicando los valores del
ángulo y la velocidad.
  * $1\leqslant \alpha \leqslant 180$.
  * $1\leqslant v \leqslant 150$.
* Se debe imprimir una sola linea con el formato:
  * "x -> Duck" si el pato alcanza.
  * "x -> Nuck" si no golpea *Nlogony*.
  * x es la distancia máxima que el proyectil alcanzó hasta llegar al suelo.
  * x tiene una precisión de 5 decimales.

## 2. A tener en cuenta: Ecuaciones fisicas

---
Para la solución de este ejercicio nos vamos a basar el la lógica planteada en un movimiento parabolico,
es decir, nos vamos a apoyar de la física, siguieendo los siguientes pasos:

1. Separar el vector de la velocidad inicial en sus dos componentes vectoriales:

    * $v_{x} = v \ast sin(\alpha)$ -> para la componente de la velocidad en $x$

    * $v_{y} = v \ast cos(\alpha)$ -> para la componente de la velocidad en $y$

    donde $\alpha$ es el ángulo de disparo y $v$ es la velocidad inicial en el que
    es lanzado el pato introducido en grados pero necesariamente debe ser convertido en
    radianes, usando esta pequeña formula de conversión:\
    $\alpha = \frac{\alpha \ast \pi}{180}$\
    Donde $\pi$ es definido en $\pi = 3.14159$

2. Para este ejercicio el problema se tiene que descomponer en dos componentes que son
la vertical y la horizontal:

* Para la componente horizontal se trabaja con MRU (Movimiento Rectilineo Uniforme)
expresanda en la siguiente ecuación:\
$x = v_{x}*t$
* Para la componentes vertical se trabaja con MRUA (Movimiento Rectilinea Uniforme
Acelerado) expresada en la siguiente ecuación:\
$y = y_{0} + v_{y} \ast t - \frac{g \ast t^{2}}{2}$\
Donde $y_{0}$ es la altura inicial referenciando a la altura de la tirachina, es decir $y_{0} = h$.\
$g$ la gravedad siendo definida en el mismo problema como $g = 9.80665$.\
$t$ el tiempo que queremos hallar.\
Para poder encontrar dicho tiempo total de vuelo la altura final debe ser igual a cero,
es decir $y = 0$, quedando como resultado la siguiente ecuación:\
$0 = h + v_{y} \ast t - \frac{g \ast t^{2}}{2}$
* Despejando esta ecuación en función del tiempo nos queda finalmente la siguiente ecucación cuadratica:\
$t = \frac{v_{y} \pm \sqrt{v_{y}^{2} - 2(g)(-h)}}{g}$\
Donde por lógica del ejercicio nos interesa unicamente la parte positiva de dicha ecuacion, es decr:\
$t = \frac{v_{y} + \sqrt{v_{y}^{2} - 2(g)(-h)}}{g}$

3. Siguiendo esta misma lógica, ahora podemos reemplazar este valor del **tiempo de vuelo total** en la
ecuación MRU y por consiguiente se encontraría la distancia **máxima** que viajaria el pato, por lo que
la ecuación definitiva y que soluciona el problema es la siguiente:\
$x = v_{x} \ast  (\frac{v_{y} + \sqrt{v_{y}^{2} - 2(g)(-h)}}{g})$

## 3. Definición de la estructura del problema

---
El ejercicio se divide en las siguientes partes:

1. El programa recibira todos los datos suministrados por le usuario que son necesarios.
2. Una vez ingresado el numero de intentos se deberá permitir ingresar la $n$ cantidad de intentos por
el usuario.
3. Se usará la formula fisica planteada en el **punto 2** para hallar al distancia máxima.
4. Cada vez que se encuentre la distancia se deberá imprimir por consola.
5. En cada intento $\alpha$ y $v$ serán redefinidos.

## 4. Programacion del problema

---
Para la programación del ejercicio se uso el lenguaje de programación *python* en su version *3.11.0*.
Para ver su solución ingresa [aqui](https://github.com/devBorisG/Complejidad_Algoritmos/blob/main/Ejercicios/Angry%20Ducks/main.py).

## 5. Recursos consumidos+

---
El tiempo de ejecución del programa mostrado en la plataforma *beecrowd* es de 0.090 segundos. Otra forma de poder evidenciar
el tiempo es con la libreria de python *time*. Este programa tiene un peso de 1.19 KB.

## 6. Tiempo invertido

---
El tiempo aproximado para la realización del código es de ***Cuarenta minutos*** (40 min).
