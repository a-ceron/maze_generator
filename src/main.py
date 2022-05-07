from turtle import shape
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

def plot(data, title):
    # define color map 
    color_map = {   1: np.array([156,137,184]), # red
                    2: np.array([240,166,202]), # green
                    3: np.array([239,195,230]),
                    4: np.array([240,230,239]),
                    5: np.array([184,190,221])} # blue 

    # make a 3d numpy array that has a color channel dimension   
    data_3d = np.ndarray(shape=(data.shape[0], data.shape[1], 3), dtype=int)
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            data_3d[i][j] = color_map[data[i][j]]

    # display the plot 
    fig, ax = plt.subplots(1,1)
    ax.imshow(data_3d)

    # add numbers to the plot 
    # thanks to tmdavison answer here https://stackoverflow.com/a/40890587/7871710
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            c = data[j,i]
            ax.text(i, j, str(c), va='center', ha='center')

    ax.set_title(title)
    plt.axis('off')
    plt.show()

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
    shape= (200,200)
    p= [0.5,0.1,0.25,0.15]

    VN= automata.automata(shape, maze.vn)
    VN.set_random( maze.states, p )
    plot( VN.get_matrix(), "Von Neumann. Iteración 0" )
    for _ in range(100):
        VN.envolve()
    plot( VN.get_matrix(), "Von Neumann. Iteración 100" )
    plot( maze.to_maze( VN.get_matrix() ), "Von Neumann. Laberinto" )
    # VN_adv= automata.automata(shape, maze.vn_adv)
    # M= automata.automata(shape, maze.moore)
    # M_adv= automata.automata(shape, maze.moore_adv)
  

if __name__ == '__main__':
    main()





