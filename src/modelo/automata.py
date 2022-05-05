# Data
# ============
from enum import Enum, EnumMeta
import numpy as np

# Visualization
# ============
from matplotlib import animation
from matplotlib.pyplot import subplots, show, close

class automata():
    def __init__(self, dim:int, phi, initial:np.arange=None ) -> None:
        self.dim = dim
        self.phi = phi
        self.matrix= initial
        if( initial is None ):
            self.matrix = np.zeros(dim)

    def set_random(self, states:int or list= None ):
        """
        set random matrix
        """
        if( isinstance(states, int) ):
            if( states is None ):
                states= 2
            self.matrix = np.random.randint( states, size=self.dim)
        elif( isinstance(states, list) ):
            self.matrix = np.random.choices( states, weights=[0.1, 0.5, 0.2, 0.2], size=self.dim )
            #self.matrix = np.random.choice( states, size=self.dim )
        elif( isinstance(states, EnumMeta) ):
            self.matrix = np.random.choice( [  x.value for x in states ], size=self.dim )
        else:
            raise Exception('states must be int or list or EnumMeta')

    def set_rule(self, rule:int):
        """
        set rule
        """
        self.rule = rule

    def get_matrix(self):
        """
        get matrix"""
        return self.matrix

    def envolve(self):
        """
        envolve matrix
        """
        self.matrix= self.phi(self.matrix)
        
   
class borders():
    def vonn_n( matrix, i,j, is_sum=False):
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
