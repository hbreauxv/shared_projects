print('Whats your name?')
name = input()
name = name.upper()
if name == 'MIKE':
    print('Hey Mike')
elif name == 'HARVEY':
    print('Hey Harvey')  
else:
    print('Hey Stranger')
    
print('Time to count!')
print('How high?')
while True:
    try:
        limit = input()
        limit = int(limit)
        break
    except ValueError:
        print("No Valid integer! Please try again ...")
counter = 0
while counter <= limit:
    print(counter)
    counter = counter + 1
