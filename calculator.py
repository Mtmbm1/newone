# Importação do math para disponibilizar a função sqrt (raiz quadrada)
import math

# Funções de adição, subtração, multiplicação e divisão
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0.0:
        return 'Cannot divide by zero'
    else:
        return x / y
    
def power(x, y):
    return x ** y

def squareroot(x):
    return math.sqrt(x)

# Função para permitir que o imput dos números aconteça depois, e não antes da seleção das operações, 
#como na primeira versão não salva do código, sem precisar repetir os inputs. 
def numbersinput():
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    return x, y
    

print ('Choose operator:')
print ('1 - Sum')
print ('2 - Subtraction')
print ('3 - Multiplication')
print ('4- Division')
print ('5 - Power')
print ('6 - Square Root')

choice = int(input('What is the number of the operator you want?:'))

if choice in [1, 2, 3, 4, 5]:
    x,y = numbersinput()

    if choice == 1: 
        print (add(x, y))
    elif choice == 2:
        print (subtract(x, y))
    elif choice == 3:
        print (multiply (x, y))
    elif choice == 4:
        print (divide(x, y))
        if y != 0.0: 
            print ('Rest:', x % y)
    elif choice == 5:
        print (power(x, y))
    else:
        print ('Invalid input, please try again!')
elif choice == 6:
    x = float(input('Digit the number:'))
    print (squareroot(x))
else:
    print ('Invalid input, please try again!')

print ('Done')
