# -*- coding: utf-8 -*-
"""Problem-04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dzKJMMOWUz2YwsKOcNYasj88I5oRssCP
"""

def  matrix_multiplication(a,b):
    new=len(a)
    list_1= []
    for i in range(new):
        list_1+= [[0]]
        for j in range(new-1):
            list_1[i]+=[0]
    for i in range (new):
        for idx in range (new):
            for k in range (new):
                first=a[i]
                second=b[k]
                third=list_1[i]
                third[idx]+=first[k]*second[idx]
    for i in list_1:
        print(i)
a=[[2,4,6],[1,3,7],[5,8,9]]
b=[[9,2,4],[4,6,7],[8,7,10]]
matrix_multiplication(a,b)