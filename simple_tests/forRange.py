while True:
    try:
        limit = int(input('How long shall we test?'))
        for i in range(limit):
            print('Testing ' + str(abs(i+1))
        break          
    except ValueError:
        continue
print('')
print('3 arguments in a for loop!')
print('')
for i in range(10, 105, 5):
    print(i)
