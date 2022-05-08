# Laberintos de automatas celulares y la busqueda de soluciones

En este trabajo usaremos autómatas celulares para la generación automática de laberintos.

## Autómata celulares 2-dimensionales
Los autómatas celulares son modelos matemáticos para sistemas en los cuales varios componentes simples actuan juntos para producir patrónes de comportamiento complejos. 
Un autómata consiste en sitios presupuestos en una rejilla. Cada sitio tomara $k$ posibles valores y será actualizada en una serie de pasos a tiempo discreto, conforme a la regla $\phi$ que depende de valor de ciertos sitios en la vecindad de este. Así el valor del sitio $i,j$ en el tiempo siguiente ($a_{i,j}^{(t+1)}$) será descrito de la siguiente forma

$$ a_{i,j}^{(t+1)} = \phi( \bf{v} ) $$

Donde $\bf{v}$ es el vector de vecinos definido en el autómata. También puede darse el caso en el que el resultado es la suma de vecinos (totalistico)

$$ a_{i,j}^{(t+1)} = f( \sum v_i ) $$

## Laberintos
Se ha encontrado en automatas celulares totalisticos patrones de laberintos que se desarrollan desde una pequeña región desordenada. Los laberintos presentan un nucle estacionario y una cascara que evolucina. 
Los automatas también presentan patrones al momento de modelar sistemas no lineares.

## Interacción entre poblaciones
En la dinámica de poblaciones se estudia cómo varía el nú- mero de sus componentes a lo largo del tiempo y los factores que influyen en dicho número Alvarez Martinez (2016).
El tamaño de una población depende, entre otros factores, de la tasa de natalidad, de la tasa de mortalidad, así como de la interacción con las especies circundantes1. Las interaccio- nes que se pueden establecer en él corresponden a dos grupos generales. El primer grupo serían las interacciones entre los seres vivos, como la simbiosis, depredación2, entre otras; y el segundo grupo serían las interacciones establecidas entre los factores abióticos (físico-químicos) del biotopo y los seres vivos que caracterizan el ecosistema

## Resultados
La implentación del código sigue el siguiente orde, se carga la biblioteca de automatas y las reglas del modelo incluidas en el script maze. Se genera un autómata dos-dimensional del tamaño especificado y se le pasa la regla que se desea implementar.

```python
import modelo.automata as automata
import modelo.maze as maze

shape= (100,100)
p= [0.5,0.1,0.25,0.15]
n= 50
# Generación del automata con las reglas del 
# problema y la vecindad de moore
M= automata.automata(shape, maze.moore)

# Genera estados aleatorios
M.set_random( maze.states, p )

# Evolucona al sistema n veces
for _ in range(n):
    M.envolve()

# Obtenemos la matris resultante
print( M.get_matrix() )

#Obtenemos la matris final que representa el laberinto
print(maze.to_maze( M.get_matrix() ))
```

Algunos resultados de la implementación se muestran abajo
![res1](./src/img/R1_M.png "Estados colocados de forma aleatoria")
![res2](./src/img/R2_M.png "Resultados después de 50 iteraciones")
![res3](./src/img/R3_M.png "Resultados después de 100 iteraciones")
![res4](./src/img/R4_M.png "Laberinto generado")