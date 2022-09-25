#!/usr/bin/env python3

'''
Unit test for main application
'''

import unittest
from unittest.mock import patch
from collections import namedtuple
from src.multipy_cli.sample import main

class SampleTest(unittest.TestCase):
    '''
    Test main application
    '''

    @patch('builtins.print')
    def test_main(self, mock_print):
        '''
        Test main function
        '''
        main()
        # Use named tuple to store different result in
        # key/value format
        Expected = namedtuple('Expected', 'index, value')
        # Test random numbers
        # Note: index start at 0 so index will
        # always be minus 1
        expected = [
            Expected(index = 1, value = ((2),)),
            Expected(index = 2, value = (('Three'),)),
            Expected(index = 4, value = (('Five'),)),
            Expected(index = 10, value = ((11),)),
            Expected(index = 14, value = (('ThreeFive'),)),
            Expected(index = 24, value = (('Five'),)),
            Expected(index = 31, value = ((32),)),
            Expected(index = 32, value = (('Three'),)),
            Expected(index = 52, value = ((53),)),
        ]

        for result in expected:
            self.assertEqual(
                mock_print.call_args_list[result.index].args,
                result.value
            )
