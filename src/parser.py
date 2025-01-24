# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:48:43 2025

@author: vanou
"""
from .lexer import lexer_tokens, addX
import numpy as np

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
    while pos < len(tokens) and tokens[pos] == '/':
        pos += 1
        next_val, pos = N(tokens, pos)
        val /= next_val
    return val, pos

# N = n | (A)

def N(tokens, pos):
    if pos < len(tokens) and isinstance(tokens[pos], (int, float, np.ndarray)):
        val = tokens[pos]
        return val, pos + 1
    if pos < len(tokens) and tokens[pos] == '(':
        val, pos = A(tokens, pos + 1)
        if pos < len(tokens) and tokens[pos] == ')':
            return val, pos + 1

def parser_string(chaine, x=1):
    tokens = lexer_tokens(chaine)
    tokens = addX(tokens, x)
    pos = 0
    val, pos = A(tokens, pos)
    return val

