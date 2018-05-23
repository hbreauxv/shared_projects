#! python3
#pw.py - An insecure password locker program. No encryption, use at your own risk

import pyperclip, pickle, os.path

#checks for password in the dictionary, copies if its there
def check_password():     
    if account in passwords:
        pyperclip.copy(passwords[account])
        print('Password for ' + account + ' copied to clipboard.')
        print('\nWould you like to update the password for ' + account + '? (y/n)')
        user_input = str.lower(input())
        if user_input == 'y':
            write_password(account)
    else:
        print('There is no account named ' + account + '\nWould you like to add that password? (y/n)')
        user_input = str.lower(input())
        if user_input == 'y':
            write_password(account)
            
#Writes password to savepasswords.pkl
def write_password(account):
    print('What\'s the password for ' + account + '?')
    password = input()
    passwords[account] = password
    save_file(passwords,'passwords')
    print('Password Saved!')

#save pw file
def save_file(passwords,name):
    with open('save'+ name + '.pkl', 'wb') as f:
        pickle.dump(passwords, f, pickle.HIGHEST_PROTOCOL)

#function to load
def load_file(name):
    with open('save' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
#Checks for password file
if os.path.isfile('savepasswords.pkl'):
    passwords = load_file('passwords')
    print('Password file found and loaded')
    print('')
else:
    #creates some dummy test passwords
    passwords = {'email': 'asdfasdfae', 'blog': 'testetstestste', 'luggage': 'supertestasfjdkl'}

while True:
    #Start of program. Asks for account name, provides help
    account = str.lower(input('What password would you like to copy?: '))

    #provides help
    if account == '' or account == '?' or account == 'help':
        print('Usage: python pw.py [account] - copy account password to clipboard\n(exit or quit to leave program)')
        continue
    elif account == 'exit' or account == 'quit':
        break

    check_password()
