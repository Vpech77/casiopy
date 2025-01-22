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
    return car in "()+-\*"

def lexeur(chaine):
    tokens = []
    
    i = 0
    
    
    

if __name__ == "__main__":
    chaine = "22x+2"
    
    tokens = []
    
    i = 0
    
    while i < len(chaine) :
        if chaine[i].isdigit():
            num = []
            while (chaine[i].isdigit() and i < len(chaine)):
                num.append(chaine[i])
                i += 1
            tokens.append(int(''.join(num)))
            break
        i += 1
        
    print(tokens)
                
                
    
    
    
    
    