import os 

samp1='C:/Users/sachi/OneDrive/Desktop/Whitehat/Project 98/sample1.txt'
samp2='C:/Users/sachi/OneDrive/Desktop/Whitehat/Project 98/sample2.txt'
temp='C:/Users/sachi/OneDrive/Desktop/Whitehat/Project 98/temp.txt'

def swap():
    data1=open(samp1,'r').read()
    data2=open(samp2,'r').read()
    open(samp1,'w').write(data2)
    open(samp2,'w').write(data1)
swap()