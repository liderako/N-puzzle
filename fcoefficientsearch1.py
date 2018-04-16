#!/usr/bin/env python

import sys
from object.Matrix import *
import numpy as np
#from read import *

def fill_row_right(matrix,row,column,size):
    global flag,max,gval
    val = matrix[row][column]
    while(column < size):
        if val == max:
            return (True)
        matrix[row][column] = val
        val += 1
        column += 1
    gval = val
    return (False)

def fill_row_left(matrix,row,column,size):
    global flag,max,sz,gval
    val = matrix[row][column]
    print "LV", val
    while(column >= size):
        if matrix[row][column] == max:
            return (True)
        matrix[row][column] = val
        val += 1
        column -= 1
    gval = val
    return (False)

def fill_column_down(matrix,row,column,size):
    global flag,max,gval
    val = matrix[row][column]
    #print "LV", val
    while(row < size):
        if matrix[row][column] == max:
            return (True)
        matrix[row][column] = val
        val += 1
        row += 1
    gval = val
    return (False)

def fill_column_up(matrix,row,column,size):
    global flag,max,sz,gval
    #if (row >= sz or column >= sz):
    #    return True
    val = matrix[row][column]
    while(row > size):
        if matrix[row][column] == max:
            return (True)
        if matrix[row][column] > 40:
            print "Mtr", matrix[row][column]
            print "Val", val
            print "row", row
        matrix[row][column] = val
        val += 1
        row -= 1
    gval = val
    return (False)

def fill_matrix1(matrix_in):
    global flag,max,sz,gval
    flag = 0
    count = 1
    sz = size = len(matrix_in)
    matrix = numpy.zeros((sz, sz))
    max = size * size - 1
    row = 0
    column = 0
    gval = matrix[row][column] = 1
    i = 1
    j = 0
    l = 0
    z = 0
    while (True):
        if fill_row_right(matrix,row,column,size - j):
            return (matrix)
        print "after right"
        if fill_column_down(matrix,row,size - i,size - j):
            return (matrix)
        print "after down"
        if fill_row_left(matrix,size - i,size - i,j):
            return (matrix)
        print "after left"
        if fill_column_up(matrix,size - i,column+j,j):
            return (matrix)
        print "after up"
        print "Z ", z
        print matrix
        z += 1
        row += 1
        column = column + j
        j += 1
        i += 1
    return (matrix)

def g_coef_count(matrix_correct,matrix_current):
    g_coef = 0    
    for i,j in enumerate(matrix_correct):
                for k,l in enumerate(j):
                        if matrix_correct[i][k] != matrix_current[i][k]:
                            g_coef += 1
    return g_coef
