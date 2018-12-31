#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 13:05:06 2018

@author: pari
"""


def returnVocabulary(descriptions):
    vocabulary = set()
    for key in descriptions.keys():
        [vocabulary.update(d.split()) for d in descriptions[key]]
    print(vocabulary)
    return vocabulary

def convertIndexToWord(vocabulary):
    ixtoword = {}
    ix = 1
    for w in vocabulary:
        ixtoword[ix] = w
        ix += 1
    return ixtoword

def convertWordToIndex(vocabulary):
    wordtoix = {}
    ix = 1
    for w in vocabulary:
        wordtoix[w] = ix
        ix += 1
    return wordtoix

def 