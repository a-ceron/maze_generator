from .automata import borders
from enum import Enum
from numpy import zeros

class states(Enum):
    BARREN= 0
    FERTILE= 1
    A= 2
    B= 3

X= lambda x, y: 1 if x==y else 0

def rules( matrix ):
    aux= zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            a= matrix[i][j]
            
            if( a == states.BARREN ):
                s= sum( map( X, borders.moore( matrix, i, j ) ), states.A )
                if s >= 2:
                    aux[i][j]= states.A
                elif s < 2: 
                    aux[i][j]= states.FERTILE
                else:
                    aux[i][j]= states.BARREN

            elif( a==states.FERTILE ):
                s_a= sum( map( X, borders.moore( matrix, i, j ) ), states.A )
                s_b= sum( map( X, borders.moore( matrix, i, j ) ), states.B )
                if( s_a >= 2 ):
                    aux[i][j]= states.A
                elif( s_a < 2 and s_b >= 2 ):   
                    aux[i][j]= states.B
                else:
                    aux[i][j]= states.FERTILE
            
            elif( a == states.A ):
                s_a= sum( map( X, borders.moore( matrix, i, j ) ), states.A )
                s_b= sum( map( X, borders.moore( matrix, i, j ) ), states.B )
                if( s_b >= 2 ):
                    aux[i][j]= states.B
                elif( s_a <= 2 and s_b < 2 ):
                    aux[i][j]= states.BARREN
                else:
                    aux[i][j]= states.A
            
            elif( a == states.B ):
                s_a= sum( map( X, borders.moore( matrix, i, j ) ), states.A )
                s_b= sum( map( X, borders.moore( matrix, i, j ) ), states.B )
                if( s_b == 8 and s_a == 0 ):
                    aux[i][j]= states.BARREN
                else:
                    aux[i][j]= states.B

    return aux
                
                
                    
            
