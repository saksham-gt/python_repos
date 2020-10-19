#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:14:37 2020

@author: sg24x7

"""
users = [
    {"id" : 0, "name" : "Hero"},
    {"id" : 1, "name" : "Dunn"},
    {"id" : 2, "name" : "Sue"},
    {"id" : 3, "name" : "Chi"},
    {"id" : 4, "name" : "Thor"},
    {"id" : 5, "name" : "Clive"},
    {"id" : 6, "name" : "Hicks"},
    {"id" : 7, "name" : "Devin"},
    {"id" : 8, "name" : "Kate"},
    {"id" : 9, "name" : "Klein"}
    ]

friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
for user in users:
    user["friends"] = []
for i, j in friendship:
    users[i]["friends"].append(users[j])        #add i as a friend of j
    users[j]["friends"].append(users[i])        #add j as a friend of i
def number_of_friends(user):
    #"""How many friends does _user_ have?"""
    return len(user["friends"])

total_connection = sum(number_of_friends(user)
                       for user in users)

from _future_ import division
num_users = len(users)
avg_users = total_connection/num_users 

#creating a list of friends of each user
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

sorted(num_friends_by_id, key=lambda(user_id, num_friends): num_friends, reverse=True)
