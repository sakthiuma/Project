#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 13:05:06 2018

@author: pari
"""
from collections import Counter
import nltk

class Vocabulary(object):
    """Simple vocabulary wrapper."""
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0

    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

    def __call__(self, word):
        if not word in self.word2idx:
            return self.word2idx['<unk>']
        return self.word2idx[word]

    def __len__(self):
        print(len(self.word2idx))
        return len(self.word2idx)


def buildVocabulary(descriptions):
    word_freq_thershold=1
    count = Counter()
    tokens=nltk.tokenize.word_tokenize(descriptions)
    print(tokens)
    count.update(tokens)
    words=[word for word,cnt in count.items() if cnt >= word_freq_thershold]
    #print(words)
    for word in words:
        vocab.add_word(word)
        
vocab = Vocabulary()  
vocab.add_word('<pad>')
vocab.add_word('<start>')
vocab.add_word('<end>')
vocab.add_word('<unk>')

        
for key in descriptions:
    for i in range(4):
        buildVocabulary(descriptions[key][i])
