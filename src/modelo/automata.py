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
        if( initial == None ):
            self.matrix = np.zeros(dim)

    def set_random(self, states:int or list= None ):
        """
        set random matrix
        """
        if( isinstance(states, int) ):
            if( states == None ):
                states= 2
            self.matrix = np.random.randint( states, size=self.dim)
        elif( isinstance(states, list) ):
            self.matrix = np.random.choice( states, size=self.dim )
        elif( isinstance(states, EnumMeta) ):
            self.matrix = np.random.choice( [  x.value for x in states ], size=self.dim )
        else:
            raise Exception('states must be int or list or EnumMeta')

    def set_rule(self, rule:int):
        """
        set rule
        """
        self.rule = rule

    def envolve(self):
        """
        envolve matrix
        """
        self.matrix= self.phi(self.matrix)
        
    def show(self, i,figsize=(10,10) ):
        """
        show matrix
        """

        fig, ax = subplots(figsize=figsize)
        im= ax.imshow(self.matrix, cmap='gray')
        ax.set_xticks(np.arange(0, self.dim[0], 1))
        ax.set_yticks(np.arange(0, self.dim[1], 1))
        ax.set_xticklabels(np.arange(0, self.dim[0], 1))
        ax.set_yticklabels(np.arange(0, self.dim[1], 1))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Automata')
        ax.grid()
        fig.tight_layout()
        fig.savefig(f'./img/automata{i}.png')
    
    def animate(self, figsize=(10,10) ):
        """
        animate matrix
        """
        fig, ax = subplots(figsize=figsize)
        im = ax.imshow(self.matrix, cmap='gray')
        def init():
            im.set_data(self.matrix)
            return [im]

        def animate(i):
            self.envolve()
            im.set_data(self.matrix)
            return [im]

        anim = animation.FuncAnimation(
                               fig, 
                               animate, 
                               init_func=init,
                               frames = 5 * 30,
                               interval = 1000 / 20, # in ms
                               )

        animation.PillowWriter()
        #anim.save('test_anim.', fps=30, )#extra_args=['-vcodec', 'libx264'])
        
        #anim = animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=1000, blit=True)

        show()


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
