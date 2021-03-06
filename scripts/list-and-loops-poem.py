#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:16:46 2018

@author: Phil
"""

import random

# set the random seed
random.seed()

# lists of words
nouns = ["words", "lines", "breath", "somethings", "insults", "jibes", "slights", "indignities", "terms", "boundaries",\
         "script", "mile mark", "book", "letter", "line in the sand", "apocrypha", "message", "letter",\
          "correspondence", "county line", "border line"]
verbs = ["laugh out loud", "speak", "recite", "hush", "break", "waste", "take", "make", "mold", \
         "roll on the floor laughing", "sleep", "read", "declaim", "roar", "cross"]
adjectives = ["saucy", "intangible", "impossible", "ineffable", "playful", "stupefied", "lobotomized", \
              "sleepy", "buxom", "arrogant","stealthy", "mechanical", "dapper", "erudite", "insatiable",\
              "breached", "ancient"]
adverbs = ["loudly", "soundly", "tersely", "playfully", "proudly", "tearfully", "mindfully", \
           "inexplicably", "boldly", "gently", "condescendingly", "disdainfully", "perfectly", "patiently"]

def random_word_choice():
    # select random words from lists
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    adverb = random.choice(adverbs)
    return noun, verb, adjective, adverb

whitespace = " "

## shuffle the list of adjectives
#random.shuffle(adjectives)

# print a sentence with random words from the lists
noun, verb, adjective, adverb = random_word_choice()
print "We speak the {noun} that we've never said.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)

noun, verb, adjective, adverb = random_word_choice()
print "You {verb} from a {noun} that you've never read.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)

noun, verb, adjective, adverb = random_word_choice()
print "Hush now, my darling, there is no need to {verb} your {noun}.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)
print whitespace 

noun, verb, adjective, adverb = random_word_choice()
print "I will {verb}".format(verb=verb)
noun, verb, adjective, adverb = random_word_choice()
print "and {verb}".format(verb=verb)
noun, verb, adjective, adverb = random_word_choice()
print "and {verb}".format(verb=verb)
noun, verb, adjective, adverb = random_word_choice()
print "and {verb}".format(verb=verb)
print "and save you from what you've become."

print whitespace 
print "The {noun} we said we would never {verb},".format(noun=noun, verb=verb)
print "have been {adjective}, and we're far past the {noun}.".format(adjective=adjective, noun=noun)
print "There is no denying you've had better days."
print whitespace
noun, verb, adjective, adverb = random_word_choice()
print "And that" 
print "{adjective}".format(adjective=adjective) 
noun, verb, adjective, adverb = random_word_choice()
print "{adjective}".format(adjective=adjective)
noun, verb, adjective, adverb = random_word_choice()
print "{adjective} person is exactly who you've become.".format(adjective=adjective)
print whitespace 

# shuffle the list of adjectives
random.shuffle(adjectives)

# print the shuffled list of adjectives with increasing whitespace
i = 0
print "You are: "
print whitespace 
for adjective in adjectives:
    i = i + 1
    whitespace = " " * i
    print whitespace + adjective
print whitespace
print "but it's okay, darling, we can work this out,"
print "Forgiveness is my middle name."
