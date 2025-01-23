# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:42:13 2025

@author: cookito
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x + 2

def draw_graph(f):
    x = np.linspace(-10, 10, 400)
    y = f(x)

    plt.plot(x, y, label='f(x)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphique de la fonction f')

    plt.legend()
    plt.grid(True)
    
def isOperator(car):
    return car in "+-\*"

def isVar(car):
    return car == 'x'

def lexer(chaine):
    tokens = []
    i = 0
    length = len(chaine)
    
    while i < length:
        if chaine[i].isdigit():
            num = []
            while (i < length and chaine[i].isdigit()):
                num.append(chaine[i])
                i += 1
            tokens.append(int(''.join(num)))
        if (i < length and isOperator(chaine[i])):
            tokens.append(chaine[i])
        if (i < length and isVar(chaine[i])):
            tokens.append(chaine[i])
        i += 1
    return tokens

def magic(left, op, right):
    return op(left, right)

def multiply(a, b):
    return a * b

def addX(tokens, x):
    new_tokens = []
    i = 0
    length = len(tokens)
    
    while i < length:
        if isVar(tokens[i]):
            if (i-1 >= 0 and isinstance(tokens[i-1], int)):
                new_tokens.pop()
                new_tokens.append(multiply(tokens[i-1] , x))
        else:
            new_tokens.append(tokens[i])
            
        i += 1
        
    return new_tokens

def parser(tokens):
    pass
                

if __name__ == "__main__":
    print("################## EQUATION ######################")
    
    chaine = "22x+256+45"
    print(chaine)
    tokens = lexer(chaine)

    magic(5, (lambda a, b: a == b), 5)
    
    tokens = addX(tokens, 2)
    print("################## TOKENS ######################")
    print(tokens)
    
    i = 0
    length = len(tokens)
    
    op = []
    nums = []
    
    while i < length:
        if i<length and not(isinstance(tokens[i], int)):
            op.append(tokens[i])
        else:
            nums.append(tokens[i])
        i += 1
    
    print("################## NUM et OPERATOR ######################")
    print(nums, op)            
    
    
        
    

    
    
    


    
    
    