# C.Thermostat

## 1. Compresión del problema

---
A este ejercicio se le obtienen los siguientes datos importantes:

* Se tienen los siguientes datos importantes:
  * $\alpha$: Valor de donde parte la temperatura
  * $\beta$: Valor donde se desea llegar
  * $l$ - $r$: limite inferior y superior respectivamente donde se puede mover la temperatura
* Se configura a la temperatura de $\alpha$
* La temperatura solo se puede configurar de $l \leqslant \alpha \leqslant r$
* La temperatura no debe variar menos de $x$
* En una operación se puede reconfigurar el termostato de la temperatura $\alpha$ a la temperatura $\beta$ si $\left| \alpha -  \beta \right| \geqslant x$  y  $l \leqslant \beta \leqslant r$
* Los datos de entrada (input) son: $l,r,x,\alpha,\beta$
* Se tiene que hallar el número minimo de operaciones necesarias para obtener la temperatura $\beta$ a partir de la temperatura $\alpha$ o decir si es imposible

## 2. Definición de la esctructura del problema

---
El ejercicio se divide en las siguientes partes:

1. Siempre se debe tener control de que los valore que se manipulen no sobrepasen lo limites

2. Se debe siempre intentar llegar a la solución que nos dan en un principio que es $\beta$ si $\left| \alpha -  \beta \right| \geqslant x$  y  $l \leqslant \beta \leqslant r$

3. Una vez ingresados los datos se debe preguntar que tan distante o cercanos estan $\alpha$ y $\beta$

## 5. Programación del problema

---
para la programación del ejercicio se uso el lenguaje de programación *python* en su versión *3.11*.
Para ver la solución ingresa [aqui](https://github.com/devBorisG/Complejidad_Algoritmos/blob/main/Ejercicios/C.Thermostat/main.py)

## 4. Recursos consumidos

---
El tiempo de ejecucion de programa en la plataforma *codeforces* es de 0.014 milisegundos con un peso de memoria inferior a 0KB

## 5. Tiempo invertido

---
El tiempo aproximado para la realización del código es de ***siete horas*** (7h).
