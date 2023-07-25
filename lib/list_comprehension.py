#!/usr/bin/env python3

def return_evens(num_list):
    return [i for i in num_list if i % 2 == 0]

# Non-list comprehension method
# new_evens = []
# for i in num_list: 
#    if i % 2 == 0:
#        new_evens.append(i)
#    else: 
#        None
# return new_evens


def make_exclamation(sentence_list):
    return [i+"!" for i in sentence_list]

#Non-list comprehension method, wasn't really working.
    # new_sentence_list = []
    # if sentence_list:
    #     for i in sentence_list: 
    #         new_sentence_list.append(i+"!")
    #     return new_sentence_list
    # else: 
    #     return new_sentence_list
