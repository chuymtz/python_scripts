# -*- coding: utf-8 -*-
"""
Python Workshop 1/30/2015

@author: yuanwang

"""
lunch = ['salad','burger','steak fries and cheesecake']

myChoice = lunch[0]

if myChoice == 'salad':
    print 'Total calories: %d' % 225
elif myChoice == 'burger':
    print 'Total calories: %d' % 335
elif myChoice.startswith('ste'):
    print 'Go to gym, now'
else:
    print 'Not sure about what you had'
