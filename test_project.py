"""Unit-test cases for class project"""
from typing_extensions import Self
import unittest

from project import show_aggie_pride, reverse_list, get_area_codes, convert_text_numbers_to_integers, convert_text_to_digits_example, area_code_lookup,  get_state_abbrev_freq



class ProjectTestCase(unittest.TestCase):
    """Unit Tests"""
    def test_show_aggie_pride(self):
        """Tests to make sure show_aggie_pride() returns the correct value"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_reverse_list(self):
        """Test to make sure reverse_list works as expected"""
        # make sure an empty list works
        self.assertFalse(reverse_list([]))

        # try numbers
        reverse = [5, 4, 3, 2, 1]
        self.assertListEqual(reverse, reverse_list([1, 2, 3, 4, 5]))

        # try letters
        reverse = ['e', 'd', 'c', 'b', 'a']
        self.assertListEqual(reverse, reverse_list(['a', 'b', 'c', 'd', 'e']))

    def test_get_area_codes(self):
        """Test to make sure we can get area codes OK"""
        ac_dict = get_area_codes()

        # Try a few known area codes
        self.assertEqual(ac_dict['516'], 'NY')
        self.assertEqual(ac_dict['919'], 'NC')
        self.assertEqual(ac_dict['212'], 'NY')
        self.assertEqual(ac_dict['970'], 'CO')

    def test_convert_text_numbers_to_integers(self):
        """Test to make sure we can convert text numbers to integers"""
        text = 'zero, one, two ,three , four,five,six,seven,eight,nine'
        results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(results, convert_text_numbers_to_integers(text))

        # test an ivnalid input
        with self.assertRaises(ValueError):
            convert_text_numbers_to_integers('zero, one, two ,three , four,five,six,seven,eight,nine,ten')

        # Empty list
        with self.assertRaises(ValueError):
            convert_text_numbers_to_integers(')')

    def test_convert_text_to_digits_example(self):
        """Test to make sure convert_text_to_digits_example works as expected"""
        text = 'zero, one, two ,three , four,five,six,seven,eight,nine'
        results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(results, convert_text_to_digits_example(text))

        with self.assertRaises(ValueError):
            convert_text_to_digits_example('ten')

        with self.assertRaises(ValueError):
            convert_text_to_digits_example('')


    def test_area_code_look(self):
        """""Test to verify if area_code_lookup works as it should"""
        text = '919-555-1212,212-555-1212 , 970-555-1212, 415-555-1212'
        output_dict = {212:'NY', 415:'CA', 919:'NC', 970:'CO'}
        self.assertEqual(output_dict, area_code_lookup(text))

        #test set of other valid area codes
        text1 = '336-554-3994, 603-554-3994, 207-654-3894, 208-654-3894'
        output_dict1 = {207:'ME', 208:'ID', 336:'NC', 603:'NH'}
        self.assertEqual(output_dict1, area_code_lookup(text1))

        #test set of invalid area codes
        with self.assertRaises(ValueError):
            area_code_lookup('105-554-3994, 800-554-3994, 877-554-3994, 888-554-3994')

        #test for empty list
        with self.assertRaises(ValueError):
            area_code_lookup('')


    def test_state_name(self):
        #Test for state_to_abb_dict    
            correct_state = 'Alaska, North Carolina, New York, New Jersey, Washington'
            statesabb = ['AK', 'NC', 'NJ', 'NY', 'WA']
            self.assertEqual(statesabb, get_state_abbrev_freq(correct_state))
        #Test for misspelled state names    
            with self.assertRaises(ValueError):  
                get_state_abbrev_freq('Alasa, North Carolina, Nue York, New Jersie, Wasinton')
        #Test for empty list
            with self.assertRaises(ValueError): 
                get_state_abbrev_freq('')        
            
if __name__ == '__main__':
    unittest.main()
