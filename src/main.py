import modelo.automata as automata
import modelo.maze as maze

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def rule_1(matrix):
    """
    Una función total para un estado definido, usando la vecindad de Von Neumann. Con fronteras cerradas
    """
    aux= np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if automata.borders.vonn_n( matrix, i, j, True ) < 4:
                aux[i][j] = 0
            else:
                aux[i][j] = 1

    return aux

def anim( ac ):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()

    
    ac.set_random( maze.states )

    def update(i):
        im_normed = ac.get_matrix()
        ax.imshow(im_normed)
        ax.set_axis_off()

        ac.envolve()

    anim = FuncAnimation(fig, update, frames=1, interval=10)

    plt.show()



def main():
    # base= np.array([
    #     [0,1,0],
    #     [1,0,1],
    #     [0,1,0]
    # ])
    # ac= automata.automata( base.shape, rule_1, base )
    
    ac= automata.automata( (50,50), maze.rules )
    anim( ac )
        
        

if __name__ == '__main__':
    main()