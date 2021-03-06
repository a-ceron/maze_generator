from .automata import borders
from enum import Enum
from numpy import zeros, where

class states(Enum):
    """Genera una clase enumerate para identificar los estados del autómata """
    BARREN= 1   # Barren soil
    FERTILE= 2  # Fertile soil
    A= 3        # autotrophe
    B= 4        # heterotrophe

# Función que identifica si una celula es de un estado
X= lambda x, y: 1 if x==y else 0

def vn( matrix ):
    """Aplicación de frontera VonNeumann

    :param matrix: Matriz del autómata
    :type matrix: np.array
    :return: Regresa una matriz con los estados actualizados
    :rtype: np.array
    """
    return rules( matrix, borders.vonn_n )

def vn_adv( matrix ):
    """Aplicación de frontera VonNeumann con frontera adiavatica

    :param matrix: Matriz del autómata
    :type matrix: np.array
    :return: Regresa una matriz con los estados actualizados
    :rtype: np.array
    """
    return rules( matrix, borders.vonn_n_adiavatic )

def moore( matrix ):
    """Aplicación de frontera Moore

    :param matrix: Matriz del autómata
    :type matrix: np.array
    :return: Regresa una matriz con los estados actualizados
    :rtype: np.array
    """
    return rules( matrix, borders.moore )

def moore_adv( matrix ):
    """Aplicación de frontera Moore con frontrera adiavatica

    :param matrix: Matriz del autómata
    :type matrix: np.array
    :return: Regresa una matriz con los estados actualizados
    :rtype: np.array
    """
    return rules( matrix, borders.moore_adiavatic )

def rules( matrix, neig  ):
    """Aplicación de las reglas del autómata

    :param matrix: Matriz de estados
    :type matrix: np.array
    :param neig: Tipo de vecindad
    :type neig: func
    :return: Matriz con los estados actualizados
    :rtype: np.array
    """
    aux= zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            #Tomamos una celula y obtenemos los vecinos
            a= matrix[i][j]
            v= neig( matrix, i, j )

            #Identidica la regla segun el estado de la celula
            if( a == states.BARREN.value ):
                s= sum( [ X( y, states.A.value ) for y in v ] )
                if s >= 2:
                    aux[i][j]= states.A.value
                elif s < 2: 
                    aux[i][j]= states.FERTILE.value
                else:
                    aux[i][j]= states.BARREN.value

            elif( a == states.FERTILE.value ):

                s_a= sum( [ X( y, states.A.value ) for y in v ] ) 
                s_b= sum( [ X( y, states.B.value ) for y in v ] )
                if( s_a >= 2 ):
                    aux[i][j]= states.A.value
                elif( s_a < 2 and s_b >= 2 ):   
                    aux[i][j]= states.B.value
                else:
                    aux[i][j]= states.FERTILE.value
            
            elif( a == states.A.value ):

                s_a= sum( [ X( y, states.A.value ) for y in v ] ) 
                s_b= sum( [ X( y, states.B.value ) for y in v ] )
                if( s_b >= 2 ):
                    aux[i][j]= states.B.value
                elif( s_a <= 2 and s_b < 2 ):
                    aux[i][j]= states.BARREN.value
                else:
                    aux[i][j]= states.A.value
            
            elif( a == states.B.value ):

                s_a= sum( [ X( y, states.A.value ) for y in v ] ) 
                s_b= sum( [ X( y, states.B.value ) for y in v ] ) 
                if( s_b == 8 and s_a == 0 ):
                    aux[i][j]= states.BARREN.value
                else:
                    aux[i][j]= states.B.value

    return aux
                
def to_maze( matrix ):
    """Transforma una matriz de estados a una matriz de bi estados o la matriz de laberinto

    :param matrix: Matriz de estados
    :type matrix: np.array
    :return: Matriz de bi estados
    :rtype: np.array
    """
    aux= where( matrix == states.B.value, matrix, states.BARREN.value)
    return where( aux == states.B.value, 5, aux)
         
def solver( matrix, rule, init:list=None ):
    """En desarrollo"""
    import numpy as np
    if( init is None ):
        init= np.random.randint(0, 5, size=(1,2) )
    matrix[init[0]][init[1]] == states.FERTILE.value
    flag= True
    while( flag ):
        vec= rule( matrix )