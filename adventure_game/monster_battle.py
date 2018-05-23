#! python 3

#monster_battle.py is a small fight game

import random

save = {'Spear Taken': False,
        'Location': 'first_room',
        'Inventory': {'Coins': 10, 'Weapon': {'Name': 'Rusty Knife', 'Damage': [2,3]}, 'Potions':2}}

slime = {'Name': 'Slime',
         'Health': random.randint(4,6),
         'Turns': 5,
         'Attacks': {'1': {'Text': 'The Slime hits you with a Big Bounce!', 'Damage': [2,4]},
                     '2': {'Text': 'The Slime hits you with a Weak Flop', 'Damage': [1,2]},
                     '3': {'Text': 'The Slime hits you with a Strong Flop!', 'Damage': [2,3]}}}

big_slime = {'Name': 'Big Slime',
             'Health': random.randint(10,13),
             'Turns': 5,
         'Attacks': {'1': {'Text': 'The Big Slime hits you with a Big Bounce!', 'Damage': [4,6]},
                     '2': {'Text': 'The Big Slime hits you with a Strong Flop', 'Damage': [2,4]},
                     '3': {'Text': 'The Big Slime hits you with a Critical Flop!', 'Damage': [5,7]},
                     '4': {'Text': 'The Big Slime hits you with a Critical Bounce!', 'Damage': [8,10]}}}

#battle(enemy) takes an enemy dictionary as input and triggers a fight with them
def battle(enemy):
    print('A ' + enemy['Name'] + ' approaches...The battle begins!')
    while True:
        damage = random.randint(*save['Inventory']['Weapon']['Damage'])
        print('You hit the ' + enemy['Name'] + ' with your ' + save['Inventory']['Weapon']['Name'] + ' for ' + str(damage) + ' damage')
        enemy['Health'] = enemy['Health'] - damage
        if enemy['Health'] > 0:    
            enemy_move = str(random.randint(1,len(enemy['Attacks'])))
            print('\n' + enemy['Attacks'][enemy_move]['Text'])
        else:
            print('\nThe ' + enemy['Name'] + ' is defeated!')
            break

battle(big_slime)







