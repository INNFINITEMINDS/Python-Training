# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 22:07:31 2017

@author: Sagar
"""

import numpy as np
import logging
import queue
logger = logging.getLogger(__name__)  #step1: create logger object

#step2: create handler object and configure (formatter and level for channel handler)
console_stream = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_stream.setFormatter(formatter)
console_stream.setLevel(logging.DEBUG)

#step3: config logger object by adding channel handler and set logging level
logger.addHandler(console_stream)
logger.setLevel(logging.DEBUG)

class CombinationFinder(object):

    def __init__(self,given, event_list):
        logger.debug("I am in Initalizer!!!")
        self.target = given
        self.events = np.array(event_list, dtype= np.float32)
        self.output = queue.deque()

    def __find_factors_coefs(self, val):
        logger.debug("I am in __find_factors_coefs!!!")
        return divmod(val, self.events)

    def compute_with_given(self):
        logger.debug("I am in compute_with_given!!!")
        m_dict = {}
        m,r = self.__find_factors_coefs(self.target)
        for event, mul, rem in zip(self.events, m, r):
            m_dict[event]= (mul, rem)
        return m_dict

    def check_mul_before_further_compute(self):
        logger.debug("I am in check_mul_before_further_compute!!!")
        _1_dict = self.compute_with_given()
        _2_dict = {}
        for k, val in _1_dict.items():
            if val[0] == 0:
                continue
            _2_dict[k] = val
        return _2_dict

    def nutralize_reminder_for_pure_factors(self):
        logger.debug("I am in nutralize_reminder_for_pure_factors!!!")
        _3_dict = self.check_mul_before_further_compute()
        for k, val in _3_dict.items():
            if  val[0] > 1 and val[1] == 0:
                self.output.append([k]*int(val[0]))
            elif val[0] > 1:
                continue
                
if __name__ == "__main__":
    given = 143
    obj = CombinationFinder(given, range(1,7))
    obj.check_mul_before_further_compute()
    obj.nutralize_reminder_for_pure_factors()
    obj.output
