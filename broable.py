#!/usr/bin/env python
#####################
# Broable
# -A function to test if a word is broable
# -Forked from a Ted Dzuiba tweet
# -
#####################

import re

BroableRegex = "^[^aeiouy]?[^aeiouy]?o[^aeiouy]?[a-z]+$"

def isBroable(word):
    return re.compile(BroableRegex).match(word) != None
