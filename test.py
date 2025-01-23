#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:21:56 2025

@author: formation
"""
tokens = [44, '+', 256, '+', 45]
stack = []

class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None
        
    def __str__(self):
        return str({"op": self.data, "left": self.left, "right": self.right})

def A(token, i):
    
    if token == '+':
        node = Node('+')
        node.left(stack.pop())
        node.right(N(token, i+1))
        
        return True
    return False
    
def F(token, i):
    
    if token == '*':
        node = Node('*')
        node.left(stack.pop())
        node.right(N(token, i+1))
        return True
    return False

def N(token, i):
    if i == len(tokens):
        return False
    
    if isinstance(token, int):
        stack.append(token)
        
    if token == '(':
        A(token, i+1)
        
    return True


if __name__ == '__main__':
    
    node = Node("+")
    node.left = 1
    node.right = 2
    

    print(node)

    i = 0
    
    while(N(tokens[i])):
        i += 1
        
    
