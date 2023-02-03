"""COMP-410 Spring 2023 Class Project"""
import requests

def add_two_numbers(num1, num2):
    """Adds two numbers together"""
    return num1 + num2

def convert_text_numbers_to_integers(text_numbers:str) -> list:
    """Convert comma separated list of numbhers zero, one, two, three, four, five, six, 
    seven, eight, nine to integers"""
    text_numbers = text_numbers.split(',')
    numbers = []
    for number in text_numbers:
        number = number.strip()
        if number == 'zero':
            numbers.append(0)
        elif number == 'one':
            numbers.append(1)
        elif number == 'two':
            numbers.append(2)
        elif number == 'three':
            numbers.append(3)
        elif number == 'four':
            numbers.append(4)
        elif number == 'five':
            numbers.append(5)
        elif number == 'six':
            numbers.append(6)
        elif number == 'seven':
            numbers.append(7)
        elif number == 'eight':
            numbers.append(8)
        elif number == 'nine':
            numbers.append(9)
        else:
            raise ValueError(f'Unknown number {number}')
    return numbers


def convert_text_to_digits_example(text: str) -> list:
    """Converts a comma seperated list of text digits to integers"""
    text_digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                   'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    results = []
    for digit in text.split(','):
        digit = digit.strip()
        if digit in text_digits:
            results.append(text_digits[digit])
        else:
            raise ValueError('Invalid digit: ' + digit)

    return results


def show_aggie_pride():
    """Show Aggie Pride"""
    return 'Aggie Pride - Worldwide'


def reverse_list(input_list) -> list:
    """Returns a list in reverse order"""
    return input_list[::-1]

def get_area_codes() -> dict:
    """Returns a dict of known area codes"""
    # Get the area code information from NANPA
    url = requests.get('https://nationalnanpa.com/nanp1/npa_report.csv', timeout=10)
    area_codes = {}
    for line in url.text.split('\n'):
        # skip the header lines
        if line.startswith('NPA') or line.startswith('File Date') or not line:
            continue
        ac_info = line.split(',')
        area_codes[ac_info[0]] = ac_info[8]
    return area_codes


if __name__ == '__main__':
    print(show_aggie_pride())



"""
Create a function which inputs a comma separated list of states and returns a dict of states and 
    total number of times each state was seen.

- The keys should be the state abbreviations, the values should be the total count.
- Sort the dictionary alphabetically by state.
- Be sure to handle variable spacing around the comma.
- In the case of an invalid or misspelled state, raise a ValueError exception.

For example:

Input text
text = 'Alaska,North Carolina,  New York , New Jersey, North Carolina, Washington'

Expected results
{'AK': 1, 'NC':2, 'NJ':1, 'NY':1, 'WA':1}

Step 1: Prepping the input (Kamaria P.)
Input is a string named as input_states as function parameter
Input needs to be broken up/separated to commas (also worry about spacing; some sort of trimming)
    - Input needs to be turned into a list named states
Need a dict of all written out states
A dictionary for each state name and mapping its abbreviation to it State_to_abb_dict
A dictionary for state frequencies (how many times it appears in input) state_freq_dict

Step 2: Iterate through input and check for valid state names (Jalen L.)
For loop to iterate through each state in "text" variable for state in states
    - check if state is in state_to_abb_dict
        -if it is: (meaning its a valid state name)
            check if state abbreviation has been added to frequency dictionary
                - if state_to_abb_dict[state] in state_freq_dict:
                    state_freq_dict[state_to_abb_dict[state]] += 1
                - else
                    state_freq_dict[state_to_abb_dict[state]] = 1
        -if not:
            - raise ValueError exception
return sorted(state_freq_dict)
"""

def get_state_abbrev_freq(text_states: str) -> dict:
    #if input was empty <--- not too sure if this will work but test is needed
    if input == "" or states == []:
        raise ValueError('Empty List')

    #non empty input
    for state in states:
        #check for valid state names
        if state in state_to_abb_dict:
            #check if state has already been added to abbreviation frequency dict
            if state_to_abb_dict[state] in state_freq_dict:
                state_freq_dict[state_to_abb_dict[state]] += 1
            #if not, add it
            else:
                state_freq_dict[state_to_abb_dict[state]] = 1
        #If invalid state name, raise ValueError
        else:
            raise ValueError('Invalid State: ' + state) 
    return sorted(state_freq_dict)