#!/usr/bin/env python
#Copyright (C) Wojciech Ziniewicz 2014

import nltk
import io
import sys
from collections import Counter
import operator

class NltkAnalyser:
    def __init__(self, filename, keyword):
        self.keyword = keyword
        with io.open(filename, 'rb') as file_handler:
            print "Opening file: %s" % file_handler
            self.raw_text = file_handler.read()
            self.tokens = nltk.word_tokenize(self.raw_text)
            self.nltk_text = nltk.Text(self.tokens)
            print "Nltk text: %s" % self.nltk_text

    def __repr__(self):
        return str(self.nltk_text)

    def concordance(self, keyword):
        return self.nltk_text.concordance(keyword)

    def collocations(self):
        return self.nltk_text.collocations()

    def wordcount(self):
        self.occurence_dict = Counter(self.nltk_text)
        self.occurence_dict_head = sorted(self.occurence_dict.items(), key=lambda x:x[1])
        self.occurence_dict_head = self.occurence_dict_head[-50:]
        print "Most common words:"
        for word in self.occurence_dict_head:
            print str(word[0]) + " " + str(word[1])

    def run(self):
        print "Concordance %s" % (self.concordance(self.keyword))
        print "Collocations %s" % (self.collocations())
        print "Most common words %s" % (self.wordcount())

if __name__ == "__main__":
    instance = NltkAnalyser(sys.argv[1], sys.argv[2])
    instance.run()
