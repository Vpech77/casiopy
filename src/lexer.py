# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:46:58 2025

@author: cookito
"""

def isOperator(car):
    return car in "+-\*()"

def isVar(car):
    return car == 'x'

def clean_string(chaine):
    for i in range(len(chaine)):
        if chaine[i] == '=':
            return chaine[i:].replace(' ', '')

def lexer_tokens(chaine):
    tokens = []
    i = 0
    chaine = clean_string(chaine)
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
    for i in range(len(tokens)):
        if isVar(tokens[i]):
            tokens[i] = x
    return tokens