# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:57:12 2017

@author: ksrir
"""
#==============================================================================
# 
# # <<Good practice to import>> the modules from higher levels
# from AppPackage.module_a import hello_A
# 
# hello_A()
# 
# 
# # <<bad practice to import>> the modules from higher levels.
# from module_a import hello_A
# 
# hello_A()
# 
#==============================================================================
# *** to do relative import it identifies the main and generate package hierarchy
# tree. if you don't have main module. 
from .module_c import hello_C

hello_C()