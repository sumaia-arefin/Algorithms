# -*- coding: utf-8 -*-
"""Problem_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QRkJ7HL8u_eYyX90f0oTX9iLbhlt7Spl
"""

#Task-02

def read():
    file=open("input2.txt","r")
    arr=[]
    for i in file:
        arr.append(i.split())
    for i in range(len(arr[1])):
        arr[1][i]=int(arr[1][i])
    testing=arr[1]
    here=int(arr[0][1])
    file.close()
    return here,testing
def write(testing,here):
    file=open("output2.txt","w")
    file.write(str(testing[0:here]))
def selectionSort(arr):
    for i in range(len(arr)):
        mins=i
        for k in range(i+1, len(arr)):
            if arr[mins]>arr[k]:
                mins=k
        new=arr[mins]
        arr[mins]=arr[i]
        arr[i]=new
here,testing=read()
selectionSort(testing)
print(testing[0:here])
write(testing,here)