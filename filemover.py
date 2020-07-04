# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:00:03 2020

@author: Aditya
"""

import csv
import os
i=0
with open('t_set.csv', newline='') as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    for row in linereader:
        i=i+1
        name = row[0]
        name=name[:-4]
        print(name)
        # Deal with the A folder
        try:
            os.rename('validation2/' + name+"png", 'validation3/' + name +"jpeg")
            print(name + " moved to new folder.")
        except FileNotFoundError:
            pass # Not found in A
        # Deal with the B folder
        '''
        try:
            os.rename('Dataset/train2/' + name, 'New folder3/' + name)
            print(name + " moved to new folder.")
        except FileNotFoundError:
            pass # Not found in B
        try:
            os.rename('Dataset/train3/' + name, 'New folder3/' + name)
            print(name + " moved to new folder.")
        except FileNotFoundError:
            pass # Not found in c
        try:
            os.rename('Dataset/train4/' + name, 'New folder3/' + name)
            print(name + " moved to new folder.")
        except FileNotFoundError:
            pass # Not found in d
        try:
            os.rename('Dataset/train5/' + name, 'New folder3/' + name)
            print(name + " moved to new folder.")
        except FileNotFoundError:
            pass # Not found in e
            
        except FileExistsError:
            pass # Name clash'''