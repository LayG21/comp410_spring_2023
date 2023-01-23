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
