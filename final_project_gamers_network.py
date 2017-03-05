#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:27:10 2017

@author: sbowie
"""

# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #

# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure.

def create_data_structure(string_input):
    likes = {}
    connections = {}
    network = [likes,connections]
    sentences = string_input.split('.')
    a = ' is connected to '
    b = ' likes to play '
    for sentence in sentences:
        name = sentence[:sentence.find(' ')]
        if a in sentence:
            connections[name] = sentence[sentence.find(a) + len(a):].split(', ')
        if b in sentence:
            likes[name] = sentence[sentence.find(b) + len(b):].split(', ')
    return network

example_network = create_data_structure(example_input)

#   Returns a list of all the connections that user has

def get_connections(network, user):
    if user in network[1]:
        return network[1][user]
    else:
        return None

#   Returns a list of all the games a user likes

def get_games_liked(network,user):
    if user in network[0]:
        return network[0][user]
    else:
        return None

#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.

def add_connection(network, user_A, user_B):
    if user_A in network[1] and user_B in network[1]:
        if user_B not in network[1][user_A]:
            network[1][user_A].append(user_B)
        return network
    else:
        return False

#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games.

def add_new_user(network, user, games):
    if user not in network[0] and user not in network[1]:
        network[0][user] = games
        network[1][user] = []
    return network

#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.

def get_secondary_connections(network, user):
    if user in network[1]:
        result = []
        for person in network[1][user]:
            for persona in network[1][person]:
                if persona not in result:
                    result.append(persona)
        return result
    else:
        return None
	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.

def count_common_connections(network, user_A, user_B):
    if user_A in network[1] and user_B in network[1]:
        count = 0
        for person in network[1][user_A]:
            if person in network[1][user_B]:
                count += 1
        return count
    return False
 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.

def find_path_to_friend(network,user_A,user_B):
    global path
    path = []
    return path_finder(network,user_A,user_B)

def path_finder(network, user_A, user_B):
    path.append(user_A)
    if user_A not in network[1] or user_B not in network[1]:
        return None
    if user_B in network[1][user_A]:
        path.append(user_B)
    else:
        for person in network[1][user_A]:
            if person not in path:
                path_finder(network,person,user_B)
            if user_B in path:
                break
    if user_B in path:
        return path
    else:
        path.pop()
        return None

#identifies other users, outside of user's existing connections, who have at least n games in common

def recommend_connections(network,user,n):
    likes = network[0][user]
    connections = network[1][user]
    recommendations = []
    for person in network[1]:
        count = 0
        for game in likes:
            if game in network[0][person] and person not in connections and person != user:
                count += 1
        if count >= n:
            recommendations.append(person)
    return recommendations

