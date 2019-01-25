#!/usr/bin/env python3

import random

# make random arrays of names, objects, maybe operations

names = [
        'Owen',
        'Caralyne',
        'Mike',
        'Bob',
        'Dave',
        'John',
        'Billy',
        'Ted',
        'Carol',
        'Millie',
        'April',
        'Kat',
        'Justin'
        ]

objects = [
        'pens',
        'cats',
        'dogs',
        'paper clips',
        'cups',
        'candy bars',
        'buttons',
        'cupcakes',
        'pizza slices',
        'books'
        ]

dict_objects = {
        'pens': 'boxes',
        'kittens': 'litters',
        'cupcakes': 'boxes',
        'buttons': 'bags'
        }

math_operation = [
        'add',
        'subtract'
        ]
answer_key = {}

for i in range(1, 11):
    random_number_of_objects = random.randrange(1,50)
    random_sets_of_objects = random.randrange(1, 6)
    random_math_operation = random.choice(math_operation)
    random_take_or_add = random.randrange(1, (random_number_of_objects * random_sets_of_objects))
    random_name = random.choice(names)
    random_object = random.choice(objects)
    random_dict_obj = random.choice(list(dict_objects.keys()))

    #print(random_dict_obj, " " , dict_objects[random_dict_obj])

    print("""
    %d ) %s has %d %s in sets of %d. If they %s %d, how many %s does %s have?
    """ % (i, random_name, random_number_of_objects, random_object, random_sets_of_objects, random_math_operation, random_take_or_add, random_object, random_name))

    if random_math_operation == 'add':
        answer = eval("%d * %d + %d" % (random_number_of_objects, random_sets_of_objects, random_take_or_add))
    elif random_math_operation == 'subtract':
        answer = eval("%d * %d - %d" % (random_number_of_objects, random_sets_of_objects, random_take_or_add))
    else:
        print("Failure")
    
    answer_key[i] = answer

for key in answer_key:
    print("Answer for Problem %d: %d" % (key, answer_key[key]))
