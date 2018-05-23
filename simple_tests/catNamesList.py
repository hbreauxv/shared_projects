

supplies = []

while True:
    print('Take some supplies..')
    supply = input('What will you take?:')
    if supply == '':
        break
    supplies = supplies + [supply]

print('You took the following:')
for i in supplies:
    print('  ' + i)

if 'Mike' in supplies:
    print('Throw away your Mike...')
    for i in supplies:
        supplies.remove('Mike')

if 'Cheese' not in supplies:
    print('You should take some cheese...')
    supplies = supplies + ['Cheese']

for i in range(len(supplies)):
    print('supply ' + str(i + 1) + ' is ' + supplies[i])

print('')
print('you have a cat')

cat = ['big', 'lazy']
size, temperment = cat

print('size is ' + size)
print ('temperment is ' + temperment)

swap = input('Want to swap?(y/n)').upper()

if swap == 'Y':
    size, temperment = temperment, size
    print('size is ' + size)
    print ('temperment is ' + temperment)
else:
    print('good call')




