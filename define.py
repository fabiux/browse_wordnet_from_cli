#!/usr/bin/python
# Browse Wordnet from CLI
# Author: Fabio Pani
from sys import argv

if len(argv) < 2:
    print('Define what?')
    exit(1)

from nltk.corpus import wordnet as wn

def explain_lemma(syn):
    print syn.name + ': ',
    for lname in syn.lemma_names:
        print lname,
    print
    print '--> ' + syn.definition
    if len(syn.examples) > 0:
        print 'Examples:'
        for example in syn.examples:
            print '- ' + example
    print


syns = wn.synsets(argv[1])
if len(syns) == 0:
    print('*** found nothing ***')
else:
    for syn in syns:
        explain_lemma(syn)
