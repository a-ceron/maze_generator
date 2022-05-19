# Data
# ============
from enum import Enum, EnumMeta
import numpy as np

# Visualization
# ============
from matplotlib import animation
from matplotlib.pyplot import subplots, show, close

class automata():
    """Crea un automata celular

    :param dim: Dimensiones del automata
    :type dim: int
    :param phi: Reglas del automata
    :type phi: function
    :param initial: Estado inicial del automata, defaults to None
    :type initial: np.arange, optional
    """
    def __init__(self, dim:int, phi, initial:np.arange=None ) -> None:
        """Constructor de la clase"""
        self.dim = dim
        self.phi = phi
        self.matrix= initial
        self.gen= 0
        if( initial is None ):
            self.matrix = np.zeros(dim)

    def set_random(self, states:int or list= None, prob:int or list=None ):
        """Inicializa los estados de la matriz

        :param states: Estados de la matriz, defaults to None
        :type states: int or list, optional
        :param prob: Vector de distribución de estados, defaults to None
        :type prob: int or list, optional
        :raises ValueError: Si no es un tipo de datos adecuado no se permite la inicialización
        """
        if( isinstance(states, int) ):
            if( states is None ):
                states= 2
            self.matrix = np.random.randint( states, size=self.dim)
        elif( isinstance(states, list) or isinstance(states, EnumMeta) ):
            if( isinstance(states, EnumMeta) ):
                states= [  x.value for x in states ]
                if( prob is None ):
                    self.matrix = np.random.choice( states, size=self.dim )
                else:
                    self.matrix = np.random.choice( states, p=prob, size=self.dim )
        else:
            raise ValueError('states must be int or list or EnumMeta')

    def set_rule(self, rule:int):
        """
        set rule
        """
        self.rule = rule

    def get_matrix(self):
        """
        get matrix"""
        return self.matrix

    def get_gen(self):
        """
        get generation
        """
        return self.gen
        
    def envolve(self):
        """
        envolve matrix
        """
        self.matrix= self.phi(self.matrix)
        self.gen+= 1
        
class borders():
    """Clase de fronteras, ahí se aplican las diferentes fornteras
    """
    def vonn_n( matrix, i, j, is_sum:bool=False):
        if( i == 0 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ 0 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == 0 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ 0 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ 0 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ 0 ] ]
            return sum( vector ) if is_sum else vector
        #Casos para los bordes
        elif( i == matrix.shape[0] - 1 and j > 0 and j < matrix.shape[1] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ 0 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( j == matrix.shape[1] - 1 and i > 0 and i < matrix.shape[0] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ 0 ] ]
            return sum( vector ) if is_sum else vector
        #Caso general
        else:
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector

    def vonn_n_adiavatic( matrix, i,j, is_sum=False):
        if( i == 0 and j == 0 ):
            vector= [ matrix[ i ][ j + 1 ], matrix[ i + 1 ][ j ] ]
            return sum( vector ) if is_sum else vector
        elif( i == 0 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i + 1 ][ j ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == 0 ):
            vector= [ matrix[ i ][ j + 1 ], matrix[ i - 1 ][ j ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i - 1 ][ j ] ]
            return sum( vector ) if is_sum else vector
        #Casos para los bordes
        elif( i == 0 and j > 0 and j < matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ i + 1 ][ j ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j > 0 and j < matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ i - 1 ][ j ] ]
            return sum( vector ) if is_sum else vector
        elif( j == 0 and i > 0 and i < matrix.shape[0] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( j == matrix.shape[1] - 1 and i > 0 and i < matrix.shape[0] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        #Caso general
        else:
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector

    def moore( matrix, i,j, is_sum=False):
        if( i == 0 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ 0 ], matrix[ i + 1 ][ 0 ], matrix[ i - 1 ][ 0 ], matrix[ i + 1 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == 0 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ 0 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ 0 ][ j + 1 ], matrix[ i - 1 ][ j + 1 ], matrix[ 0 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ 0 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ 0 ], matrix[ 0 ][ 0 ], matrix[ i - 1 ][ 0 ], matrix[ 0 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        #Casos para los bordes
        elif( i == matrix.shape[0] - 1 and j > 0 and j < matrix.shape[1] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ 0 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ 0 ][ j + 1 ], matrix[ i - 1 ][ j + 1 ], matrix[ 0 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( j == matrix.shape[1] - 1 and i > 0 and i < matrix.shape[0] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ 0 ], matrix[ i + 1 ][ 0 ], matrix[ i - 1 ][ 0 ], matrix[ i + 1 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        #Caso general
        else:
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ i + 1 ][ j + 1 ], matrix[ i - 1 ][ j + 1 ], matrix[ i + 1 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector

    def moore_adiavatic( matrix, i,j, is_sum=False):
        if( i == 0 and j == 0 ):
            vector= [ matrix[ i ][ j + 1 ], matrix[ i + 1 ][ j ], matrix[ i + 1 ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == 0 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i + 1 ][ j ], matrix[ i + 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == 0 ):
            vector= [ matrix[ i ][ j + 1 ], matrix[ i - 1 ][ j ], matrix[ i - 1 ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j == matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i - 1 ][ j ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        #Casos para los bordes
        elif( i == 0 and j > 0 and j < matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ i + 1 ][ j ], matrix[ i + 1 ][ j + 1 ], matrix[ i + 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( i == matrix.shape[0] - 1 and j > 0 and j < matrix.shape[1] - 1 ):
            vector= [ matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ i - 1 ][ j ], matrix[ i - 1 ][ j + 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( j == 0 and i > 0 and i < matrix.shape[0] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j + 1 ], matrix[ i + 1 ][ j + 1 ], matrix[ i - 1 ][ j + 1 ] ]
            return sum( vector ) if is_sum else vector
        elif( j == matrix.shape[1] - 1 and i > 0 and i < matrix.shape[0] - 1 ):
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i + 1 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
        #Caso general
        else:
            vector= [ matrix[ i - 1 ][ j ], matrix[ i + 1 ][ j ], matrix[ i ][ j - 1 ], matrix[ i ][ j + 1 ], matrix[ i + 1 ][ j + 1 ], matrix[ i - 1 ][ j + 1 ], matrix[ i + 1 ][ j - 1 ], matrix[ i - 1 ][ j - 1 ] ]
            return sum( vector ) if is_sum else vector
