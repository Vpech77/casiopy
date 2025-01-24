# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:42:13 2025

@author: cookito
"""
import matplotlib.pyplot as plt
import numpy as np
from src.parser import parser_string

def draw_graph(chaine):
    x = np.linspace(-10, 10, 400)
    y = parser_string(chaine, x)
    fig = plt.figure()
    plt.plot(x, y, label=f'{chaine}', color='red')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graphique de la fonction {chaine}')

    plt.legend()
    plt.grid(True)


if __name__ == "__main__":
    chaine = "y = 22 * x + 3"
    draw_graph(chaine)
    
    chaine = "y = 5*x*x + 3*x"
    draw_graph(chaine)
    
    chaine = "(23+78)*26"
    res = parser_string(chaine)
    print(res)
    
    chaine = "12 + (3*(4+5)+12) / 2"
    res = parser_string(chaine)
    print(res)
    

            
    

    
    
    


    
    
    