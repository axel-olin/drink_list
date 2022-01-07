#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:59:29 2021

@author: bolin
"""

#%%

def read_drink_list(file, name):

    ### Import functions
    import os
    import re
    os.chdir('/Users/bolin/Dropbox/Drinks/Code')
    from classes import drink, drink_list, ingredient
    
    
    ### Function
    #Initialize drink list
    final_list = []

    # Read file
    with open(file) as f:
        Imode = False
        Rmode = False
        
        for line in f:
            # Keep track of type
            if line[0:2] == '#T':
                currtype = line[3:len(line)]
                continue
            
            # Start a new drink
            if line[0:2] == '#N':
                currdrink = drink(line[3:len(line)].splitlines()[0], currtype)
                continue
            
            # Add ingredients
            if line[0:2] == '#I':
                Imode = True
                continue
            
            if line[0:2] == '#i':
                Imode = False
                continue
            
            if Imode:
                I = line.splitlines()[0]
                I = re.split('\t+', I)
                currdrink += ingredient(I[0], float(I[1]), I[2])
                continue
            
            # Add instructions
            if line[0:2] == '#R':
                Rmode = True
                instructions = []
                continue
       
            if line[0:2] == '#r':
                Rmode = False
                currdrink.set_instructions(instructions)
                final_list.append(currdrink)
                continue     
       
            if Rmode:
                instructions.append(line.splitlines()[0])
                continue
            
    book = drink_list(name)
    for drink_variable in final_list:
        book += drink_variable
        
    return book

#%%

def read_bar(file, name, location):
    """Reads a file with directory 'file' which contains comma-
    separated values of bar inventory. Name becomes the name of the bar
    and location becomes the location of the bar"""
   
    ### Import functions
    import os
    os.chdir('/Users/bolin/Dropbox/Drinks/Code')
    from classes import ingredient, ingredient_list, drink, bar, drink_list


    ### Function    
    #Initialize bar
    local = bar(name, location)

    # Read file
    with open(file) as f:
        for line in f:
            line = line.splitlines()[0]
            line = line.split(',')
            
            local += ingredient(line[0], line[1], line[2], line[3])
            
    return(local)

#%%

def write_bar(bar, file):
    """Writes ingredients in bar to file.
    This function overwrites whatever is present in file."""
    
    ### Import funcitons
    import csv
    
    
    ### Write data
    with open(file, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        for ingredient in bar.get_dict().values():
            temp_list = [ingredient.get_name(), ingredient.get_units(), ingredient.get_unittype(), ingredient.get_category()]

            writer.writerow(temp_list)