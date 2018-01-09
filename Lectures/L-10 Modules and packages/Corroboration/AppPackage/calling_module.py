# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 03:53:23 2017

@author: ksrir

Important: 
    Add full package path into Tools> PYTHONPATH manager
    (or)
    from sys import path
    path.insert(0,<<Full path of package in all the script path of the package>>)
"""



# All import must be fully refered from main package.
# All imports must be in alphebetical order.
# All imports 

from AppPackage.module_a import hello_A 
from AppPackage.subPackage.module_c import hello_C

hello_A()
hello_C()

#import with out using main app package <<not a good practice>>
from module_b import hello_B
from subPackage.module_c import hello_C

hello_B()
hello_C()

#relative import types <<not a good programming practice>>.

