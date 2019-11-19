# fibonacci.py

def fib():
    fibs = [1, 2]
    #count = 1
    #num = 0
    #cant = 0
    #fibs = []
    for i in range(1,9):

        fib_n = fibs[i] + fibs[i-1]
        fibs.append(fib_n)
        '''
        while num < 100:
            #print (count)
            num = num + 1
            cont = cant
            cant = count
            count = cont + cant
            fibs.append(count)
        '''
        ''' 
        implement Fibonacci sequence to calculate the 
        first 10 Fibonacci numbers, note Fn = Fn-1 + Fn-2
        '''

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
