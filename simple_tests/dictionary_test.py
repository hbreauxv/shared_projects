#Dictionary Testing

months = {'January': 31, '01': 31, 'February': 28, 'March': 31}
#print(months['January'])

#user_month = input('Calender for what month?: ')

#for i in range(1,months[user_month]+1,1):
    #print('------')
    #print(str(i) + '   |')

print(months.values())

print(31 in months.values())
print('mouse' in months.values())


#while True:
   # dictionary_search = (input('Search the dictionary for: '))
   # try:
        #if dictionary_search == '':
            #break
      #  elif int(dictionary_search) in months.values():
          #  print(dictionary_search + ' is in the dictionary')
           # break
      #  else:
           # print(dictionary_search + ' isnt in the dictionary. Search nothing to quit')
   # except ValueError:
       # print(dictionary_search + ' isnt in the dictionary.  Search a number or search nothing to quit')

        

#key = input('What do you want to add to the dictionary? ')
#value = input('What value should ' + str(key) + ' have?')
#months[key] = value
#print(str(key) + ' is equal to ' + str(months[key]))


print(months.items())

for k, v in months.items():
    print(str(k) + ' = ' + str(v))

