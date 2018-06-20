import shutil, os, re

# Regex to match dates, doesnt care if date is valid or not
datePattern = re.compile(r"(.*)(\d\d).(\d\d).(\d\d\d\d)(.*)")

# Ask the user whether they want to switch to American or European style dates for their files

date_type = str.lower(input('Switch to American or European?'))

# Check that input was american or european
while date_type != 'american' and date_type != 'european':
    date_type = str.lower(input('Invalid date type.  Type "American" or "European"'))

# Loop through the files in our current directory
for file in os.listdir():

    # Search the file to see if we get match for our datePattern regex
    mo = datePattern.search(file)

    # Skip the file if it doesnt have a date in it
    if mo == None:
        continue

    # Define the different sections of the filename
    start = mo.group(1)
    day = mo.group(2)
    month = mo.group(3)
    year = mo.group(4)
    end = mo.group(5)

    # Swap the month and day
    swapped_name = start + month + '.' + day + '.' + year + end

    # Check if the new date is valid, skip the swap if it isn't

    if date_type == 'american':
        if int(month) >= 13:
            print('Invalid American Date, Skipping %s ...' % (file))
            continue

    if (date_type) == 'european':
        if int(day) >= 13:
            print('Invalid European Date, Skipping %s...' % (file))
            continue

    # Get the Abs directory, and then join the old + new filename to the end of it
    absDir = os.path.abspath('.')
    old_full_name = os.path.join(absDir, file)
    new_full_name = os.path.join(absDir,swapped_name)

    # Replaces the old filename with the new, swapped one
    shutil.move(old_full_name,new_full_name)