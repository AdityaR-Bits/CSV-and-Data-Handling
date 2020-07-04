# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:57:32 2020

@author: Aditya
"""

import csv
import os

from os import listdir
from os.path import isfile, join
i=-1
filename = "hey_set.csv"
fields = ['', 'image', 'quality', 'DR_grade']
onlyfiles = [f for f in listdir("validation2") if isfile(join("validation2", f))]
#print(len(onlyfiles))
listtaken=[]
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for name in onlyfiles:
        #print(name)
        with open('Label_EyeQ_test.csv', newline='') as csvfile2:
            linereader = csv.reader(csvfile2, delimiter=',')
            #print(len(linereader))
            for row in linereader:
                #print(row)
                nameofcsv = row[1]
                
                nameofcsv=nameofcsv[:-4]
                if name[:-3]==nameofcsv:
                    i=i+1
                    rowpaste=[row[1],row[2], row[3]]
                    listtaken.append(rowpaste)
                    print(i)
    csvwriter.writerows(listtaken)
                    
                        
     
                    

                    
        
   
        