# mr Miyagi trainee ##project

# Ask for user input and depending on the response, mr Miyagi will respond.
phrase = input('Student: ')

#Evaluate each input and print the appropriate responses
while phrase != 'Sensei, I am at peace':
    if phrase[:6] != 'Sensei':
        print('Sensei: You are smart, but not wise - address me as Sensei please')
        phrase = input('Student: ')
    elif phrase[-1] == '?':
        print('Sensei: Questions are wise, but for now. Wax on, and Wax off!')
        phrase = input('Student: ')
    elif 'block' in phrase:
        print('Sensei: Remember, best block, not to be there..')
        phrase = input('Student: ')
    else:
        print('Sensei: Do not lose focus. Wax on. Wax off')
        phrase = input('Student: ')

if phrase == 'Sensei, I am at peace':
    print('Sensei: Sometimes, what heart know, head forget')


# Follow these rules:

# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'

# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'

# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'

# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'

# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')