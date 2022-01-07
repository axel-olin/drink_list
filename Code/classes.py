#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:34:00 2021

@author: bolin
"""

import copy


#%%
###### ingredient and subclasses ######
### ingredient ###´
class ingredient(object):
    """An ingredient is the name of a specific drink
    ingredient as well as the number and type of units availble"""
    
    ### Basics
    # Initialization
    def __init__(self, name, units, unittype, category = 'Empty'):
        """Initializes the names variable and amount"""
        self._name = name
        self._units = float(units)
        self._unittype = unittype
        self._category = category

    # Printing
    def __str__(self):
        """Returns the names of the ingredient and
        the number of units left"""
        return str(self._units) + ' ' + str(self._unittype) + ' of ' + self._name


    ### Setters
    # Add number to _units
    def add_units(self, number):
        """Adds 'number' of units to the stock.
        'number' is an integer"""
        self._units += number
        
    # Remove number from _units
    def remove_units(self, number):
        """Remove 'number' of units from the stock
        'number' is an integer"""
        if self._units - number < 0:
            raise ValueError('The number of units cannot be below 0')
        self._units -= number

    # Set _units to specific value
    def set_units(self, number):
        """Sets 'number' of units to a specific value.
        'number' is an integer"""
        self._units = number
    
    # Set _category to specific value
    def set_category(self, category):
        """Sets 'category' of ingredient to a specific value"""
        self._category = category
    

    ### Getters
    def get_name(self):
        """ Returns the name of the ingredient"""
        return self._name
    
    def get_units(self):
        """Returns the current number of units"""
        return self._units
    
    def get_unittype(self):
        """Returns the type of units"""
        return self._unittype
    
    def get_category(self):
        """ Returns the category of the ingredient"""
        return self._category

#%%

###### ingredient_list and subclasses ######
### ingredient_list ###
class ingredient_list(object):
    """An ingredient_list is essentially a dictionary of ingredients.
    Ingredients have to be unique within the list and has to be of
    type ingredient or any subclass of ingredient"""
    
    ### Basics
    # Initialization
    def __init__(self, name):
        """Initializes an empty ingredient dictionary"""
        self._ingredient_dict = {}
        self._name = name
    
    # Length of ingredient list
    def __len__(self):
        """Returns the length of the ingredient list"""
        return len(self._ingredient_dict)
    
    
    ### Setters
    # Set name of the dictionary
    def set_name(self, name):
        """Changes the name of the ingredient_list to 'name'"""
        self._name = name
        
    # Add ingredient to ingredient list
    def add_ingredient(self, ingredient):
        """ Adds an ingredient to the dictionary.
        Assumes ingredient is of type 'ingredient' or a subtype."""
        self._ingredient_dict[ingredient.get_name()] = ingredient
    
    # Remove ingredient from ingredient list
    def remove_ingredient(self, ingredient):
        """Removes an ingredient with name 'ingredient' from the dictionary."""
        self._ingredient_dict.pop(ingredient)


    ### Getters
    # Get name of ingredient list    
    def get_name(self):
        """Extract the name of the ingredient list"""
        return self._name

    # Get a specific ingredient from the dictionary
    def get_ingredient(self, ingredient):
        """Extract a specific ingredient from the dictionary"""
        try:
            return self._ingredient_dict[ingredient]
        except:
            raise ValueError('Ingredient not in inventory')
            
    # Get the full ingredient dictionary
    def get_dict(self):
        """Extract the ingredient dictionary"""
        return self._ingredient_dict
            
    
    ### Printing
    # Print the inventory
    def print_ingredient_list(self):
        """Prints the full ingredient list"""
        print('The ingredient list of ' + self._name + ' is as follows:')
        for k in self._ingredient_dict.values():
            print(k)


    ###### Numerical actions on list
    ### Addition ###
    def __add__(self, other):
        """"Assumes other to be either ingredient or ingredient_list.
        Makes a copy of self and then adds ingredients from the
        dictionary of 'other' to the new copy. If the ingredient is already
        present, the unit values are simply added. If the ingredient is not yet
        present, a new entry is created. The list is then returned."""
        
        
        ### ingredient ###
        if isinstance(other, ingredient):
            temp = copy.deepcopy(self)

            ### If ingredient doesn't yet exist
            if other.get_name() not in temp._ingredient_dict.keys():
                temp.add_ingredient(other)
                
                
            ### If ingredient already exists
            else:
                # Check that units are the same
                if other.get_unittype() != temp._ingredient_dict[other.get_name()].get_unittype():
                    raise ValueError("Unit's are not equal")
                
                #Add value to ingredient
                currvalue = other.get_units()
                temp._ingredient_dict[other.get_name()].add_units(currvalue)
    
            return temp
        
        ### ingredient_list ###
        if isinstance(other, ingredient_list):
            temp = copy.deepcopy(self)
        
            ### Check that ingredients have the same units
            for a in other.get_dict():
                if a in temp._ingredient_dict.keys():
                    if other.get_ingredient(a).get_unittype() != temp._ingredient_dict[a].get_unittype():
                        raise ValueError("Unit's are not equal")
    
        
            ### Loop through ingredient_list of other
            for a in other.get_dict():
                
                # If ingredient doesn't yet exist
                if a not in temp._ingredient_dict.keys():
                    temp.add_ingredient(other.get_ingredient(a))     

                # If ingredient already yet exists
                else:
                    currvalue = other.get_ingredient(a).get_units()
                    temp._ingredient_dict[a].add_units(currvalue)
            
            return temp   


    ### Self addition ###
    def __iadd__(self, other):
        """"Assumes other to be either ingredient or ingredient_list.
        Simply adds ingredients from the dictionary of 'other' to self. 
        If the ingredient is already present, the unit values are simply
        added. If the ingredient is not yet present, a new entry is created."""
               
        ### ingredient ###
        if isinstance(other, ingredient):
            ### If ingredient doesn't exist
            if other.get_name() not in self._ingredient_dict.keys():
                self.add_ingredient(other)
    
    
            ### If ingredient already exists
            else:
                # Check that units are the same
                if other.get_unittype() != self._ingredient_dict[other.get_name()].get_unittype():
                    raise ValueError("Unit's are not equal")
                
                #Add value
                currvalue = other.get_units()
                self._ingredient_dict[other.get_name()].add_units(currvalue)
                
            return self
        
        ### ingredient_list ###
        if isinstance(other, ingredient_list):
            ### Check that ingredients have the same units
            for a in other.get_dict():
                if a in self._ingredient_dict.keys():
                    if other.get_ingredient(a).get_unittype() != self._ingredient_dict[a].get_unittype():
                        raise ValueError("Unit's are not equal")

            
            ### Loop through ingredient_list of other
            for a in other.get_dict():
                
                # If ingredient already exists
                if a in self._ingredient_dict.keys():
                    currvalue = other.get_ingredient(a).get_units()
                    self._ingredient_dict[a].add_units(currvalue)

                # If ingredient doesn't yet exists
                else:
                    self.add_ingredient(other.get_ingredient(a))
            
            return self 
    

    ### Subtraction
    def __sub__(self, other):
        """"Assumes other to be either ingredient or ingredient_list.
        Makes a copy of self and then subtracts ingredients of the
        dictionary of 'other' from the new copy. If the ingredient is already
        present, the subtraction is made only if the result is nonnegative,
        otherwise, an error is shown. If the ingredient is not yet
        present, an error is also shown. At the end, the list is returned."""
        
        
        ### ingredient ###
        if isinstance(other, ingredient):
            temp = copy.deepcopy(self)
        
            ### If ingredient doesn't exist
            if other.get_name() not in temp._ingredient_dict.keys():
                raise ValueError("Can't remove ingredient that doesn't exist")

            ### If ingredient exists
            else:
                # Check that units are the same
                if other.get_unittype() != temp._ingredient_dict[other.get_name()].get_unittype():
                    raise ValueError("Unit's are not equal")

                # Remove value
                currvalue = other.get_units()
                temp._ingredient_dict[other.get_name()].remove_units(currvalue)
                
                # Remove ingredient if == 0
                if temp._ingredient_dict[other.get_name()].get_units() == 0:
                    temp.remove_ingredient(other.get_name())
                
            return temp
        
        ### ingredient_list ###
        if isinstance(other, ingredient_list):
            temp = copy.deepcopy(self)
    
            ### Check that ingredients exist and have the same units
            for a in other.get_dict():
                # Check that ingredients exist
                if a not in temp._ingredient_dict.keys():
                    raise ValueError('Ingredient ' + a + ' doesnt exist')

                #Check that units are equal
                if a in temp._ingredient_dict.keys():
                    if other.get_ingredient(a).get_unittype() != temp._ingredient_dict[a].get_unittype():
                        raise ValueError("Unit's are not equal")
        
    
            ### Loop through ingredient_list of other
            for a in other.get_dict():
                # Remove value
                currvalue = other.get_ingredient(a).get_units()
                temp._ingredient_dict[a].remove_units(currvalue)

                #Remove ingredient if ==0
                if temp._ingredient_dict[a].get_units() == 0:
                    temp.remove_ingredient(a)
            
            return temp   
      
        
    ### Self subtraction
    def __isub__(self, other):
        """"Assumes other to be either ingredient or ingredient_list.
        Subtracts ingredients of the dictionary of 'other' from self. 
        If the ingredient is present, the 'other' value is simply
        subtracted. If the ingredient is not yet present, an error is thrown."""
               
        ### ingredient ###
        if isinstance(other, ingredient):
  
            ### If ingredient doesn't exist
            if other.get_name() not in self._ingredient_dict.keys():
                raise ValueError("Can't remove ingredient that doesn't exist")
                
    
            ### If ingredient already exists
            else:
                # Check that units are the same
                if other.get_unittype() != self._ingredient_dict[other.get_name()].get_unittype():
                    raise ValueError("Unit's are not equal")

                # Add value    
                currvalue = other.get_units()
                self._ingredient_dict[other.get_name()].remove_units(currvalue)

                # Remove ingredient if == 0
                if self._ingredient_dict[other.get_name()].get_units() == 0:
                    self.remove_ingredient(other.get_name())  
                
            return self
   
        ### ingredient_list ###
        if isinstance(other, ingredient_list):
            ### Check that ingredients exist and have the same units
            for a in other.get_dict():
                # Check that ingredient exists
                if a not in self._ingredient_dict.keys():
                    raise ValueError("Can't remove ingredient that doesn't exist")
                    
                #Check that units are equal
                if a in self._ingredient_dict.keys():
                    if other.get_ingredient(a).get_unittype() != self._ingredient_dict[a].get_unittype():
                        raise ValueError("Unit's are not equal") 
                        
            
            ### Loop through ingredient_list of other
            for a in other.get_dict():
                # Add value
                currvalue = other.get_ingredient(a).get_units()
                self._ingredient_dict[a].remove_units(currvalue)

                # Remove ingredient if == 0
                if self._ingredient_dict[a].get_units() == 0:
                    self.remove_ingredient(a)
            
            return self 
    
    
    ### Multiplication
    def __mul__(self, integer):
        """"Makes a copy of self, multiplies the unit values for all 
        ingredients with 'integer', and returns a new ingredient_list item."""        
        temp = copy.deepcopy(self)
        for a in temp._ingredient_dict:
            curr = temp._ingredient_dict[a].get_units()
            temp._ingredient_dict[a].set_units(curr * integer)
        return temp
            
    
    
### drink ###
class drink(ingredient_list):
    """Drink is a subclass of ingredient_list with some additional attributes"""
    ### Basics
    # Initialization
    def __init__(self, name, drink_class):
        super().__init__(name)
        self._drink_class = drink_class
        self._instructions = None
    
    ### Setters
    # Add drink instructions
    def set_instructions(self, instructions):
        """Adds instructions in the form of a string. Each row of the string starts
        with a number and contains one step in the order of exectution"""
        self._instructions = instructions


    ### Getters
    # Get drink instructions
    def get_instructions(self):
        """Extracts the instructions"""
        return self._instructions


    ### Printing
    # Print instructions
    def print_instructions(self):
        """Prints the instructions of the drink"""
        print('Instructions:')        
        for k in self._instructions:
            print(k)


### bar ###
class bar(ingredient_list):
    """Bar is a subclass of ingredient_list with some additional attributes"""
    ### Basics
    # Initialization
    def __init__(self, name, bar_location):
        super().__init__(name)
        self._bar_location = bar_location
        
    
    ### interactions with drink_list ###
    # Check which drinks can be made
    def can_make(self, drink_list):
        
        # Loop through drink_list
        available = {}
        
        for drink in drink_list.get_dict().values():
            
            # Check that all drink ingredients exist in the bar
            drink_ingredients = set(drink.get_dict().keys())
            bar_ingredients = set(self.get_dict().keys())
            
            if not drink_ingredients.issubset(bar_ingredients):
                continue
            
            # Loop through drink ingredients
            min_ingredient = []
            
            for ingredient in drink.get_dict().values():
                #Calculate number of units usable
                units = self.get_dict()[ingredient.get_name()].get_units() // ingredient.get_units()
                min_ingredient.append(units)
            
            #If minimum is < 1, don't list drink
            if min(min_ingredient) < 1:
                continue
            
            #Add minimum to available list
            available[drink.get_name()] = min(min_ingredient)
            
        return available
        
        
#%%        

###### drink_list and subclasses ######
### drink_list ###
class drink_list(object):
    """A drink_list is a dictionary of drinks.
    Drinks have to be unique within the list and have to be of
    type drink"""
    
    ### Basics
    # Initialization
    def __init__(self, name):
        """Initializes an empty drink list"""
        self._drink_dict = {}
        self._name = name
    
    # Length of drink list
    def __len__(self):
        """Returns the length of the drink list"""
        return len(self._drink_dict)
    
    
    ### Setters
    # Set name of the dictionary
    def set_name(self, name):
        """Changes the name of the drink_list to 'name'"""
        self._name = name
        
    # Add drink to drink list
    def add_drink(self, drink):
        """ Adds a drink to the dictionary.
        Assumes drink is of type 'drink'."""
        self._drink_dict[drink.get_name()] = drink
    
    # Remove drink from drink list
    def remove_drink(self, drink):
        """Removes the drink with name 'drink' from the dictionary."""
        self._drink_dict.pop(drink)


    ### Getters
    # Get name of drink list    
    def get_name(self):
        """Extract the name of the drink list"""
        return self._name

    # Get a specific drink from the dictionary
    def get_drink(self, drink):
        """Extract a specific drink from the dictionary"""
        try:
            return self._drink_dict[drink]
        except:
            raise ValueError('Drink not in inventory')
    
    # Get the full drink dictionary
    def get_dict(self):
        """Extract the full drink dictionary"""
        return self._drink_dict
            
    ### Printing
    # Print the drink names
    def print_names(self):
        """Prints the names of the drinks in the list"""
        print('The drink list ' + self._name + ' contains the following drinks:')
        for k in self._drink_dict.keys():
            print(k)
        print('')
        
        

    def print_recipes(self):
        """Prints out the full recipes of each drink """
        for k in self._drink_dict.values():
            print('******' + k.get_name() + '******')
            k.print_ingredient_list()
            print('')
            k.print_instructions()
            print('\n')

    ###### Numerical actions on list
    ### Addition
    def __add__(self, other):
        """"Assumes other to be of object type drink or drink_list.
        Makes a copy of self and then adds 'drink' or drinks from the
        dictionary of 'other' to the new copy. If the drink is already
        present, the original object is replaced and a warning message is sent."""
        
        
        # ingredient
        if isinstance(other, drink):
            temp = copy.deepcopy(self)
        
            #If drink already exists
            if other.get_name() in temp._drink_dict.keys():
                temp.add_drink(other)
                UserWarning('Drink ' + drink.get_name() + ' was replaced.')
    
            #If ingredient doesn't yet exists
            else:
                temp.add_drink(other)
                
            return temp
        
        # ingredient_list
        if isinstance(other, drink_list):
            temp = copy.deepcopy(self)
        
            for a in other.get_dict():
                
                #If ingredient already exists
                if a in temp._drink_dict.keys():
                    temp.add_drink(a)
                    UserWarning('Drink ' + drink.get_name() + ' was replaced.')

                #If ingredient doesn't yet exists
                else:
                    temp.add_drink(a)
            
            return temp   

    ### Self addition
    def __iadd__(self, other):
        """"Assumes other to be either drink or drink_list.
        Simply adds drinks from the dictionary of 'other' to self. 
        If the ingredient is already present, the drink is added
        and a warning is shown. If the ingredient is not yet present,
        a new entry is created."""
               
        # drink
        if isinstance(other, drink):
            #If drink already exists
            if other.get_name() in self._drink_dict.keys():
                self.add_drink(other)
                UserWarning('Drink ' + drink.get_name() + ' was replaced.')
    
            #If drink doesn't yet exists
            else:
                self.add_drink(other)
                
            return self
        
        # drink_list
        if isinstance(other, drink_list):
            #Loop through drinks in drink_list
            for a in other.get_dict():
                
                #If drink already exists
                if a in self._drink_dict.keys():
                    self.add_drink(a)
                    UserWarning('Drink ' + drink.get_name() + ' was replaced.')

                #If drink doesn't yet exists
                else:
                    self.add_drink(a)
            
            return self 
   