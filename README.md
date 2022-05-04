# Laberintos de automatas celulares y la busqueda de soluciones

En este trabajo usaremos autómatas celulares para la generación automática de laberintos.

## Autómata celulares 2-dimensionales
Los autómatas celulares son modelos matemáticos para sistemas en los cuales varios componentes simples actuan juntos para producir patrónes de comportamiento complejos. 
Un autómata consiste en sitios presupuestos en una rejilla. Cada sitio tomara $k$ posibles valores y será actualizada en una serie de pasos a tiempo discreto, conforme a la regla $\phi$ que depende de valor de ciertos sitios en la vecindad de este. Así el valor del sitio $i,j$ en el tiempo siguiente ($a_{i,j}^{(t+1)}$) será descrito de la siguiente forma

$$ a_{i,j}^{(t+1)} = \phi( \bf{v} ) $$

Donde $\bf{v}$ es el vector de vecinos definido en el autómata. También puede darse el caso en el que el resultado es la suma de vecinos

$$ a_{i,j}^{(t+1)} = f( \sum v_i ) $$