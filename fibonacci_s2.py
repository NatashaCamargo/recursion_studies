# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:37:28 2021

@author: Natasha Camargo
"""
def fibonacci(n):
  if n < 0:
    return "It's Negative"
  if n == 1:
    return 1
  if n == 0:
    return 0
  if n >=2:  
    return fibonacci(n-1) + fibonacci(n-2)
