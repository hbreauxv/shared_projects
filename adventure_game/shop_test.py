#!/usr/bin/python

#adventure_game.py is a text based adventure game, mainly created to practice dictionaries and functions.
#It quickly got a little out of hand. It features a save system, battle system, and shop/inventory system
#as well as multiple rooms to explore.  There is currently no way to "Beat" the game. 

import pickle, os.path, random

#enemy dictionaries, used in battle()
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

#creates the first room
def first_room():
    while True:
        save_game('Location','first_room')
        print('')
        print('Theres a shop in front of you.')
        print('')
        print('(Type "Shop" to Shop!)')
        print('(Type "Inventory" to check your items!)')
        print('(Type "Leave" to quit!)')
        player_input = str.lower(input('What do: '))
        print('')
        if player_input == 'look':
            print('You see something beyond the shop...')
        elif player_input == 'shop':
            store()
        elif player_input == 'inventory':
            show_inv()
        elif player_input == 'forward' or player_input == 'go forward':
            a2()
        elif player_input == 'leave':
            break
        else:
            print('You cant do that here')
            
#battle(enemy) takes an enemy dictionary as input and triggers a fight with them
def battle(enemy):
    print('A ' + enemy['Name'] + ' approaches...The battle begins!')
    while True:
        damage = random.randint(*save['Weapon']['Damage'])
        print('You hit the ' + enemy['Name'] + ' with your ' + save['Weapon']['Name'] + ' for ' + str(damage) + ' damage')
        enemy['Health'] = enemy['Health'] - damage
        if enemy['Health'] > 0:    
            enemy_move = str(random.randint(1,len(enemy['Attacks'])))
            print('\n' + enemy['Attacks'][enemy_move]['Text'])
        else:
            print('\nThe ' + enemy['Name'] + ' is defeated!')
            break
        
#function to show the player inventory              
def show_inv():
    print('You have the following items...')
    print('')
    print('Weapon: ' + save['Weapon']['Name'] + ', Damage ' + str(save['Weapon']['Damage']))
    for k, v in save['Inventory'].items():
        print(str(k) + ': ' + str(v))
    print('')

#function for the store
def store():
    save_game('Location','store')
    store_prices = {'Sword': 5, 'Potion': 3}

    print('Welcome to the store!')
    print('')
    print('We sell the following...')
    for k, v in store_prices.items():
        print(str(k) + ' for ' + str(v) + ' coins')
        
    while True:
        print('')
        print('You have ' + str(save['Inventory']['Coins']) + ' coins...')
        print('(type leave to exit the store)')
        buy = str.lower(input('What do you want to buy?'))
        print('')
        #Player Buys a Swords
        if buy == 'sword':
            if  save['Weapon']['Name'] != 'Sword':
                if save['Inventory']['Coins'] >= store_prices['Sword']:
                    print('You bought the Sword!')
                    save['Weapon'] = {'Name': 'Sword', 'Damage': [2,4]}
                    save['Inventory']['Coins'] = save['Inventory']['Coins'] - store_prices['Sword']
                else:
                    print('You dont have enough money for that!')
            else:
                print('You already have a Sword!')

        #Player buys a potion
        elif buy == 'potion':
            if save['Inventory']['Coins'] >= store_prices['Potion']:
                print('You bought a Potion!')
                save['Inventory']['Potions'] = save['Inventory']['Potions'] + 1
                save['Inventory']['Coins'] = save['Inventory']['Coins'] - store_prices['Potion']
                print(save['Inventory']['Potions'])
            else:
                print('You dont have enough money for that!')

        #Player looks
        elif buy == 'look':
            print('You see a crusty shopkeeper and not much else')

        #Player leaves
        elif buy == 'leave':
            break

        #Player buys something that isn't in the shop
        else:
            print('We dont sell any ' + buy + ' here!')
            print('')
    print('')
    print('You left the store.')

def a2():
    while True:
        print('')
        save_game('Location','a2')
        if save['Spear Taken'] != True:
            print('You see a rusty spear...')
            player_input = str.lower(input('What do: '))
            if player_input == 'take' or player_input == 'take spear':
                print('You take the spear...it looks...painful.')
                save['Weapon'] = {'Name':'Rusty Spear', 'Damage':[3,4]}
                save['Spear Taken'] = True
            elif player_input == 'inventory':
                show_inv()
            elif player_input == 'leave' or player_input == 'go back' or player_input == 'back':
                first_room()
            elif player_input == 'forward':
                a3()
            else:
                print('You cant do that here')
        else:
            print('The room is empty...')
            player_input = str.lower(input('What do: '))
            if player_input == 'inventory':
                show_inv()
            elif player_input == 'leave' or player_input == 'go back' or player_input == 'back':
                break
            elif player_input == 'forward':
                a3()
            else:
                print('You cant do that here')

def a3():
    while True:
        print('')
        save_game('Location','a3')
        print('You see a load of slimes in front of you...they looks like they want a battle')
        player_input = str.lower(input('What do: '))
        #player fights the slime
        if player_input == 'fight' or player_input == 'battle':
            #1/3 chance to fight big_slime, 2/3 chance to fight slime
            if random.randint(1,3) == 3:
                battle(big_slime)
            else:
                battle(slime)
        elif player_input == 'inventory':
            show_inv()
        elif player_input == 'back' or player_input == 'leave':
            break
        else:
            print('You cant do that here')

#Save Player Save File
def save_file(save,name):
    with open('save'+ name + '.pkl', 'wb') as f:
        pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
        
#Load Player Save File
def load_file(name):
    with open('save' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def save_game(k,v):
    global save
    save[k] = v
    save_file(save,'test')

#Store Price Variables , Not Currently Used.  
low_price = [3,1]
normal_price = [5,2]
high_price = [7,3]


#Checks for existence of save file, loads if it exists, else create save
if os.path.isfile('savetest.pkl'):
    save = load_file('test')
    #inventory = load_file('inventory')
    print('Your journey continues...')
    print('')
else:
    save = {'Spear Taken': False,
        'Location': 'first_room',
        'Weapon': {'Name': 'Rusty Knife', 'Damage': [2,3]},
        'Inventory': {'Coins': 10,  'Potions':2}}

#Starts the game!
while True:
    #starts the game at the player location in save['Location']
    globals()[save['Location']]()
    break
    
print('Thanks for playing!')
