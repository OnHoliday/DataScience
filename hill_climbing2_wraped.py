import os
clear = lambda: os.system('cls')
clear()

import random



def maxer(l):
    x = l[0]
    for i in range(len(l)):
        if l[i] > x:
            x = l[i]
    return (x,l.index(x))

def random_matrix_maker(n,m):
    a = [0] * n
    for q in range(n):
        a[q] = [0] * m
        
    for q in range(n):
        for w in range(m):
            a[q][w] = random.randint(1,n*m*10)
    return a

def matrix_maker(n,m):
    a = [0] * n
    for q in range(n):
        a[q] = [0] * m
    x = 1
    for q in range(n):
        for w in range(m):
            a[q][w] = x
            x+=1
    return a

def neighborhood(a, n , m, i ,j):
    if (i in {0, n-1}) and (j in {0, m-1}):
        if i == 0:
            if j == 0:
                neighbors = [0 , a[i][j+1] , 0 , a[i+1][j]]
            else: neighbors = [a[i][j-1] , 0 , 0 , a[i+1][j]]
        else:
            if i == n-1:
                if j == 0:
                    neighbors = [0 , a[i][j+1], a[i-1][j] , 0] 
                else: neighbors = [a[i][j-1], 0 , a[i-1][j] , 0] 
    elif (i in {0,n-1}) or j in {0,m-1}:      
            if i == 0:
                neighbors = [a[i][j-1] , a[i][j+1] , 0 , a[i+1][j]]
            elif i == n-1:
                neighbors = [a[i][j-1] , a[i][j+1] , a[i-1][j] , 0]
            elif j == 0:
                neighbors = [0 , a[i][j+1] , a[i-1][j] , a[i+1][j]]
            elif j == m-1:
                neighbors = [a[i][j-1] , 0 , a[i-1][j] , a[i+1][j]]
    else: 
        neighbors = [a[i][j-1] , a[i][j+1] , a[i-1][j], a[i+1][j]]
    neighbors.append(a[i][j])
    return neighbors

def execute_function(function_name, rows, columns):
    return {
        'random': lambda : random_matrix_maker(rows, columns),
        'consecutive': lambda: matrix_maker(rows, columns),
    }[function_name]()
    
  

def hill_climbing(rows, columns, function_name):  # Tu trzeba zdefiniowac metodę uzupełniania pol w macierzy czy random czy koljenosc czy whatever

    # Create matrix 
    
    a = execute_function(function_name,rows,columns)  
    
    # Chose starting point at random
    i = random.randint(0,rows-1)
    j = random.randint(0,columns-1)
    
    print('\nStarting point was in %d. row and %d. column with value %d \n' % (i+1, j+1 ,a[i][j]))
    
    # Look for maximium
    temp_max = 0
    local_max = a[i][j]
    counter = 0
    
    # iterate until not be able to move to better point
    while local_max > temp_max:
        temp_max = a[i][j]
        # function creating a list of neighbors
        neighbors = neighborhood(a,rows,columns,i,j)
        if maxer(neighbors)[1] == 0:
            j-=1
        elif maxer(neighbors)[1] == 1:
            j+=1
        elif maxer(neighbors)[1] == 2:
            i-=1
        elif maxer(neighbors)[1] == 3:
            i+=1
        elif maxer(neighbors)[1] == 4:
            break
        counter+=1
        local_max = a[i][j]
        print('We moved to %d. row and %d. column with value %d' % (i+1, j+1 ,a[i][j]))
    
    # Present output
    print('\nLocal minimum is %d and was found in %d. iteration.' % (local_max, counter))
    print('Local minimum is in %d. row and %d. column in the matrix below: \n' % (i+1, j+1))
    for s in a:  
        print(*s)

n = int(input('\nEnter the number of rows in matrix: '))
m = int(input('\nEnter the number of columns in matrix: '))
c = str(input('\nEnter the name of function which will be used to fill matrix: '))

hill_climbing(n,m,c)

