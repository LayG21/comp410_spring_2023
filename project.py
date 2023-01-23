"""COMP-410 Spring 2023 Class Project"""
import requests


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
