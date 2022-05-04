import modelo.automata as automata
import modelo.maze as maze
from numpy import zeros


def rule_1(matrix):
    """
    Una función total para un estado definido, usando la vecindad de Von Neumann. Con fronteras cerradas
    """
    aux= zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if automata.borders.moore( matrix, i, j, True ) > 3:
                aux[i][j] = 1
            else:
                aux[i][j] = 0

    return aux

def main():
    for state in maze.cell_states:
        print(state)

        
        

if __name__ == '__main__':
    main()