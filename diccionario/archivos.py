""" with open('data1.txt', 'w') as ejemplo:
    ejemplo.write('curso de phyton\n')
    ejemplo.write('grupo 10\n')
    ejemplo.write('PIO\n') """
    

""" with open('data1.txt', 'r') as ejemplo:
    print(ejemplo.read()) """

""" with open('data1.txt', 'a') as ejemplo:
    ejemplo.write('\n')
    ejemplo.write('final') """


with open('data1.txt', 'r') as ejemplo:
    next = ejemplo.readline()
    print(next)