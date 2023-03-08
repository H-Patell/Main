#!/usr/bin/env python
# coding: utf-8
 
from googlesearch import search
import os

def Get_URL(dish, n=5, stop=5):

    f=open(dish+".txt","x")     #creating files with dish name
    f.close()
    f=open(dish+".txt","a")     #writing in the created file in append mode
    query = dish + ' recipe +"ingredients" -youtube'
    for i in search(query, tld = 'co.in', num = n, stop = stop, pause = 5):
        f.write(i+"\n")         #separating each link by a "\n"
    f.close()
    return ('url generated')
