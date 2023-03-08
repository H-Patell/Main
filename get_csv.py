#!/usr/bin/env python
# coding: utf-8
import string
from googlesearch import search
import os
import time
from bs4 import BeautifulSoup
import requests
import html2text
import shutil
from pre_processing import *        #--------------------
import concurrent.futures


#to read all the links in the given file
def read_text_file(parent, file_path):
    #parent = os.path.join(parent, "chinese_csv")
    #try:
    #    os.mkdir(parent)    #to overcome error due to already existing folder
    #except:
    c = 1
    with open(file_path, 'r') as f:
        new_list = f.read().split("\n")     #converting the links into a list

    # print(new_list)
    # print(new_list) 
    #path = os.path.splitext(file_path)[0]   #getting file name without txt to create folder
    #try:
    #    os.mkdir(path)      #making a directory with dish name
    #    os.chdir(path)      #going inside directory with dish name
    #except:
    #    return

    new_list.pop()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for link in new_list:
            f = executor.submit(func,c,link)       #list comprehension
            # print(f.result())
            c = c+1


    # for link in new_list:
    #     Get_HTML(c,link)
    #     c = c+1                 #keeping count of link number

    # print(f"ended for {path}")
    #shutil.move(path,parent)    #moving the new dish folder into the /FINAL/RECIPE folder

#to read .txt files from the CHINESE FOLDER
def read_file(str):

    parent = r'C:\Users\Admin\capstone\14-10-2022\OLD'  #link access path
    path = os.path.join(parent,str)
    os.chdir(path)
    c=0
    k = 0

    for file in os.listdir():
    # Check whether file is in text format or not
        if file.endswith(".txt"):
            if(c<5):
                file_path = f"{path}/{file}"
                c = c+1
                # call read text file function
                read_text_file(parent, file_path)
            else:
                # time.sleep(1000)
                # print("slept for 1000 s")
                c=0
    return ('csv files generated')

#calling function for CHINESE folder
if __name__ == '__main__':
    read_file(r'C:\Users\Admin\capstone\14-10-2022\OLD')#

#    finish  = time.perf_counter()

#    print(f'Finished in {round(finish-start,2)} seconds(s)')