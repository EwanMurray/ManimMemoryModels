# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from os import chdir, getcwd
wd=getcwd()
chdir(wd)

# import
import quail
import pandas

#load data
egg = quail.load('example')

# analyze and plot
fegg = egg.analyze('spc', listgroup=['average']*8)

fegg.plot(title='Serial Position Curve')
