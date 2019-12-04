# Write a bizz and zzuu game ##project

# write a program that take a number
# number = int(input('Choose a number: '))
# if number%5 == 0 and number%3 ==0:
#     print('bizzzzuu')
# elif number%5 == 0:
#     print('zzuu')
# elif number%3 ==0:
#     print('bizz')
# else:
#     print(number)

def bizzzzuu_game(number):
    if number%5 == 0 and number%3 ==0:
        return 'bizzzzuu'
    elif number%3 ==0:
        return 'bizz'
    elif number%5 == 0:
        return 'zzuu'
    else:
        return number

user_input = int(input('Enter a limit number: '))
for number in range(1,user_input):
    print(bizzzzuu_game(number))

# prints back each individual number, but

    # if it is a multiple of 3 it returns bizz

    # if a multiple of 5 it return zzuu

    # if a multiple of 3 and 5 it return bizzzzuu

# Learn about how to define a function

# remember what is DRY?

# what is separation of concerns?

# Turn this into a functional program



# Definition of done for the project:

# This should be it's own project
# it should have a read me
# it should outline the project

    # it should have simple instructions on how to run the project

# it should have git and git history
# it should be on git hub