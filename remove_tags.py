#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 17:20:13 2017

@author: sbowie
"""

# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def split_string(source,splitlist):
	words = []
	atsplit = True #atsplit
	for char in source: #iterate through string by each character
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				words.append(char)
				atsplit = False
			else:
				#add character to last word
				words[-1] = words[-1] + char
	return words

def remove_tags(source):
    words = []
    inside_tag = False
    at_split = True
    for char in source:
        if char == '<':
            inside_tag = True
        if char == ' ' or inside_tag == True:
            if char == '>':
                inside_tag = False
            at_split = True
        else:
            if at_split:
                words.append(char)
                at_split = False
            else:
                words[-1] += char
    return words

print remove_tags('''<h1>Title</h1><p>This is a <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']