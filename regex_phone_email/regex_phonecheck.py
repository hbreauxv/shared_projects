#! python 3
"""regex_phone_email.py takes text in your clipboard, parses phone numbers
and email addresses from it, and pastes just the numbers and emails into
your clipboard.
"""

import re, pyperclip

# write search results to paste global in readable form
def regex_paste(regex):
    for i in range(len(regex)):
        global paste
        area, number = regex[i]
        paste = paste + area + number + '\n' 

# initialize paste Global
paste = ''

# regex for phone and email address 
phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d\-\d\d\d\d)')
emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@+[a-zA-Z0-9._%+-]+)(\.[a-zA-Z0-9._%+-]+)')

# search copied text for phone numbers
numbers = phoneNumRegex.findall(pyperclip.paste())
regex_paste(numbers)    # copy numbers to paste global

# search copied text for emails
emails = emailRegex.findall(pyperclip.paste())
regex_paste(emails)     # copy emails to paste global

# paste the paste global into clipboard
pyperclip.copy(paste)




