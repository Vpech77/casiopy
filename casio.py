# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:42:13 2025

@author: cookito
"""
import matplotlib.pyplot as plt
import numpy as np

def draw_graph(chaine):
    x = np.linspace(-10, 10, 400)
    y = parser(chaine, x)

    plt.plot(x, y, label='f(x)')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphique de la fonction f')

    plt.legend()
    plt.grid(True)
    
def isOperator(car):
    return car in "+-\*()"

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

def addX(tokens, x):
    new_tokens = []
    i = 0
    
    while i < len(tokens):
        if isVar(tokens[i]):
            if i == 0:
                new_tokens.append(x)
            if i-1 >= 0:
                if isinstance(tokens[i-1], int):
                    new_tokens.pop()
                    new_tokens.append(tokens[i-1]*x)
                # x alone
                else:
                    new_tokens.append(x)
        else:
            new_tokens.append(tokens[i])
        i += 1
    return new_tokens

# A = F (+ F)*

def A(tokens, pos):
    val, pos = F(tokens, pos)
    while pos < len(tokens) and tokens[pos] == '+':
        pos += 1
        next_val, pos = F(tokens, pos)
        val += next_val
    return val, pos

# F = N (* N)*

def F(tokens, pos):
    val, pos = N(tokens, pos)
    while pos < len(tokens) and tokens[pos] == '*':
        pos += 1
        next_val, pos = N(tokens, pos)
        val *= next_val
    return val, pos

# N = n | (A)

def N(tokens, pos):
    if pos < len(tokens) and isinstance(tokens[pos], (int, float, np.ndarray)):
        val = tokens[pos]
        return val, pos + 1
    if pos < len(tokens) and tokens[pos] == '(':
        val, pos = A(tokens, pos+1)
        if pos < len(tokens) and tokens[pos] == ')':
            return val, pos + 1

def parser(chaine, x):
    tokens = lexer(chaine)
    tokens = addX(tokens, x)
    print(tokens)

    pos = 0
    val, pos = A(tokens, pos)
    return val

if __name__ == "__main__":
    print("################## EQUATION ######################")
    
    chaine = "22x*x+45"
    
    print(chaine)
    
    val = parser(chaine, 2)
    
    draw_graph(chaine)
    
    
    


    
    
    