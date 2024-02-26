import random


def validate_input(prompt): # take and validate input
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print('No one is joining for the party')
                exit()
            else:
                return value
        except ValueError:
            print('You must enter number!')


def list_of_guests(num_guests):  # Make a dictionary with guests
    print('Enter the name of every friend (including you), each on a new line:')
    guest_dict = {input(): 0 for _ in range(num_guests)}
    return guest_dict


def split_bill(guest_dict, total, lucky_or_not):  # Calculating split bil, with or without lucky feature.
    if lucky_or_not == 'Yes':
        lucky_one = lucky_function(guest_dict)
        guest_dict = {key: round(total / (len(guest_dict) - 1), 2) for key in guest_dict}
        guest_dict[lucky_one] = 0
        return f'{lucky_one} is the lucky one!\n{guest_dict}'
    else:
        guest_dict = {key: round(total / len(guest_dict), 2) for key in guest_dict}
        return f'No one is going to be lucky\n{guest_dict}'


def lucky_function(guest_dict):  # Lucky feature that returns who's lucky.
    lucky = random.choice(list(guest_dict.keys()))
    return lucky


def main():  # well, self expl
    num_guests = validate_input('Enter the number of friends joining (including you):\n')
    guest_list = list_of_guests(num_guests)
    total_bill = validate_input('Enter the total bill value:\n')
    lucky_one = input('Do you want to use the "Who is lucky?" feature? Write Yes/No\n')
    print(split_bill(guest_list, total_bill, lucky_one))


main()
