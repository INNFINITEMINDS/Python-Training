# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 19:19:03 2017

@author: ksrir
"""
from .module_a import hello_A

def hello_B():
    print("I am a function from SubPackage.module_b.py!!!")
    
def hello_A_B():
    hello_B()
    print("Eecuting relatively import function hello_A!!!")
    hello_A()
        
if __name__ == "__main__":
    ## write module testing call here.
    pass