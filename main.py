# Automate Creating and Sending Mails:

with open('./Automated-Mail-Sender/demo_file.txt') as data:
    content = data.read()
    
with open('./Automated-Mail-Sender/names.txt') as name:
    collect = name.read()
    take = collect.splitlines() # list of all names in list
        
    # iterate the take list
    for _ in take:
        with open(f'./Automated-Mail-Sender/Letter_to_{_}.txt', 'w') as f1:
            modify = content.replace('[name]', _)
            f1.write(modify)