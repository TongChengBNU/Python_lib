# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 07:20:17 2020

@author: 75934
"""

import jieba

txt = open(r"data\threekingdoms.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):
    word, count = items[1]
    print("{0:<10}{1:>5}".format(word, count))