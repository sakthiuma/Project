#!/usr/bin/env python28
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 13:23:12 2018

@author: pari
"""

from caption_preprocess import preprocess
from utilities import *

descriptions = dict()
descriptions = preprocess()
vocabulary = returnVocabulary(descriptions)

#Prepare descriptions for training
 

wordtoix = convertWordToIndex(vocabulary)
print(wordtoix)

ixtoword = convertIndexToWord(vocabulary)
print(ixtoword)