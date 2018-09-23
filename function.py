# ###########################################
# #########Gernerator liczb Fibonaciego######
# ###########################################
  
def get_fibo(ile):
    nr_fib = []
    nr_fib.append(1)
    nr_fib.append(1)
    i=2
    if ile >=2:
        while i <= ile:
            nr_fib.append(nr_fib[i-1] + nr_fib[i-2])
            i+=1
    print(nr_fib[ile])
    
get_fibo(116)  

# ###########################################
# ####### Zamienia sys 10 na 2 ##############
# ###########################################

def zmieniacz_binarny(liczba):
    binar = 0
    while liczba >= 1:  
        temp = 1
        licznik = 0
        while liczba >= temp:
            temp *= 2
            licznik += 1
        binar += 10 ** (licznik-1) 
        liczba -= 2 ** (licznik-1)
    print(binar)


zmieniacz_binarny(127)

# ###########################################
# ####### Zamienia sys 2 na 10 ##############
# ###########################################

def zmieniacz_dziesietny(liczba):
    dziesietna = 0
    a = list(str(liczba)) 
    while len(a)>0:
        if a[0] == '1':
            dziesietna += 2 ** (len(a)-1)
        del a[0]
    print(dziesietna)
    
    
zmieniacz_dziesietny(101101)