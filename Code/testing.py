#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:58:13 2021

@author: bolin
"""
import os
os.chdir('/Users/bolin/Dropbox/Drinks/Code')

from classes import ingredient, ingredient_list, drink, bar, drink_list
from reading_and_writing import read_drink_list, read_bar, write_bar


#%%

###### Testing ######
### drink_list ###
# Assemble drink list
book = read_drink_list('/Users/bolin/Dropbox/Drinks/Documents/drink_list.txt', "Axel's recipe book")

# Print names
book.print_names()
book.print_recipes()


### inventory ###
#Assemble inventory
local = read_bar('/Users/bolin/Dropbox/Drinks/Documents/bar.csv', "Axel's bar", '22 Rue de Grenelle')

#Print inventory
local.print_ingredient_list()

#Remove some drinks
local -= book.get_drink('Old fashioned')
local.print_ingredient_list()

#Remove some more drinks
local -= book.get_drink('Daiquiri') * 3
local.print_ingredient_list()

#Remove that doesn't work
local -= book.get_drink('Sazerac')
local.print_ingredient_list()

#Test which drinks are available
local.can_make(book)

#Write to file
write_bar(local, '/Users/bolin/Dropbox/Drinks/Documents/bar.csv')
