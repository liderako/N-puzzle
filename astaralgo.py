#!/usr/bin/env python

import sys
from object.Matrix import *
import numpy as np
#from read import *

def check_row_right(matrix,row,column,size):
    global flag,max
    val = matrix[row][column]
    while(column < size):
        print matrix[row][column]
        if matrix[row][column] != val:
            if matrix[row][column] == 0 and matrix[row][column - 1] == max:
                flag = 1
            return (True)
        val += 1
        column += 1
    return (False)

def check_row_left(matrix,row,column,size):
    global flag,max
    val = matrix[row][column]
    while(column >= size):
        print matrix[row][column]
        if matrix[row][column] != val:
                return (True)
        val += 1
        column -= 1
    return (False)

def check_column_down(matrix,row,column,size):
    global flag,max
    val = matrix[row][column]
    while(row < size):
        print matrix[row][column]
        if matrix[row][column] != val:
                return (True)
        val += 1
        row += 1
    return (False)

def check_column_up(matrix,row,column,size):
    global flag,max
    val = matrix[row][column]
    while(row > size):
        print matrix[row][column]
        if matrix[row][column] != val:
                return (True)
        val += 1
        row -= 1
    return (False)

def check_solve(matrix):
    global flag,max
    flag = 0
    count = 1
    size = len(matrix)
    max = size * size - 1
    row = 0
    column = 0
    i = 1
    j = 0
    while (True):
        if check_row_right(matrix,row,column,size - j):
            if flag:
                return (True)
            return (False)
        #column = size - i
        #size -= j
        if check_column_down(matrix,row,size - i,size - j):
            return (False)
        #row = size - i
        #print ("Size - j" + str(size - j))
        #print ("Size - i" + str(size - i))
        #print ("Size " + str(size))
        if check_row_left(matrix,size - i,size - i,j):
            return (False)
        if check_column_up(matrix,size - i,column,j):
            return (False)
        row += 1
        column = column + j
        j += 1
        i += 1
        #print row
        #return (True)
    return (True)

'''
        if (j != count):
                return (False)
            count += 1
    return (True)
'''
