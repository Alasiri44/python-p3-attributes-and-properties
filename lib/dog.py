#!/usr/bin/env python3
import re

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,breed=APPROVED_BREEDS[0], name='fido',):
        self.name = name
        self.breed = breed

    def get_name(self):
        print('Getting the name')       
        return self._name
        
    def set_name(self, name):
        # print(f'Setting the name equal to {name}')
        if(type(name) != str) or (len(name) > 25) or (len(name) < 1) or (not re.search('[a-zA-Z]',name)):
            print("Name must be string between 1 and 25 characters.")        
        elif(0 < len(name) < 25):
            self._name = name
            
    def get_breed(self):
        print('Getting the breed')       
        return self._breed

    def set_breed(self, breed):
        if(breed not in APPROVED_BREEDS):  
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed
            
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
    
