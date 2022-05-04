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
            v= borders.moore( matrix, i, j )

            if( a == states.B.value ):
                s= sum( [ X( y, states.A.value ) for y in v ] )
                if s >= 2:
                    aux[i][j]= states.A.value
                elif s < 2: 
                    aux[i][j]= states.FERTILE.value
                else:
                    aux[i][j]= states.B.value

            elif( a==states.FERTILE.value ):

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
                    aux[i][j]= states.B.value
                else:
                    aux[i][j]= states.A.value
            
            elif( a == states.B.value ):

                s_a= sum( [ X( y, states.A.value ) for y in v ] ) 
                s_b= sum( [ X( y, states.B.value ) for y in v ] ) 
                if( s_b == 8 and s_a == 0 ):
                    aux[i][j]= states.B.value
                else:
                    aux[i][j]= states.B.value

    return aux
                
                
                    
            
