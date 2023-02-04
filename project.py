"""COMP-410 Spring 2023 Class Project"""
import requests
import re

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


def email_domain_and_user_count(string_of_emails):
    dict_of_emails_and_users_count = {}
    seen_emails = set()
    if not string_of_emails:
        return dict_of_emails_and_users_count
    email_list = re.findall(r'[\w\.-]+@[\w\.-]+', string_of_emails)
    for email in email_list:
        if not re.match(r'[\w\.-]+@[\w\.-]+', email):
            raise ValueError(f"{email} is not a valid email address")
        email_domain = email.split('@')[1]
        if email not in seen_emails:
            seen_emails.add(email)
            if email_domain not in dict_of_emails_and_users_count:
                dict_of_emails_and_users_count[email_domain] = 1
            else:
                dict_of_emails_and_users_count[email_domain] += 1
    
    return dict(sorted(dict_of_emails_and_users_count.items()))

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

def area_code_lookup(phone_nums:str) -> dict:
    """Returns a dict of area codes and corresponding state"""
    phone_list = sorted(phone_nums.replace(" ", "").split(","))
    output_dict = {}
    for num in phone_list:
        area_code = num[0:3]
        if ~bool(re.match(num, '/\d{3}-\d{3}-\d{4})/')) & (int(area_code) > 200):
            output_dict[int(area_code)] = get_area_codes().get(area_code)
        else:
            raise ValueError('Invalid phone number: ' + num)
    return output_dict

if __name__ == '__main__':
    print(show_aggie_pride())
