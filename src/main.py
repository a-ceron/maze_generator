import modelo.automata as automata
import modelo.maze as maze

import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt



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
        ax.imshow(im_normed, cmap='Accent')
        ax.set_axis_off()
        ax.set_title(f"Iteración {i}")
        print(ac.get_gen())
        ac.envolve()

        return [im_normed]

    anim = FuncAnimation(fig, update, frames=200, interval=10)

    
    plt.show()



def main():
    # base= np.array([
    #     [0,1,0],
    #     [1,0,1],
    #     [0,1,0]
    # ])
    # # ac= automata.automata( base.shape, rule_1, base )

    shape= (100,100)
    p= [0.5, 0.1, 0.3, 0.1]
    ac= automata.automata( shape, maze.rules )
    #anim( ac )


    ac.set_random( maze.states, prob=p )
    ac.envolve()
    init= ac.get_matrix()

    # print(ac.get_gen())
    # for i in range(100):
    #     ac.envolve()
    # t_1oo= ac.get_matrix()
    # print(ac.get_gen())

    # for i in range(100):
    #     ac.envolve()
    # t_2oo= ac.get_matrix()
    # print(ac.get_gen())

    fin= maze.to_maze( init )

    plt.imshow(init, cmap='rainbow')
    plt.show()
    # plt.imshow(t_1oo, cmap='rainbow')
    # plt.show()
    # plt.imshow(t_2oo, cmap='rainbow')
    # plt.show()
    plt.imshow(fin, cmap='rainbow')
    plt.show()
        
        

if __name__ == '__main__':
    main()