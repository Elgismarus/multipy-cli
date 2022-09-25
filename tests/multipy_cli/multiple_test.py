#!/usr/bin/env python3

'''
Unit test for Multiple class
'''

import unittest
from unittest.mock import patch
from src.multipy_cli.multiple import Multiple

class MultipleTest(unittest.TestCase):
    '''
    Test class Multiple
    '''

    def test_convert(self):
        '''
        Test convert method
        '''
        arr = Multiple.convert(
            [3,5,11,15],
            Multiple(3, 'Three'),
            Multiple(5, 'Five')
        )

        self.assertEqual(arr, [
            'Three',
            'Five',
            11,
            'ThreeFive',
        ])

    @patch('builtins.print')
    def test_analyse_with_callback(self, mock_print):
        '''
        Test convert with callback method
        '''
        Multiple.convert(
            [3,5,11],
            lambda result: print(result),
            Multiple(3, 'Three'),
            Multiple(5, 'Five')
        )

        self.assertEqual(mock_print.call_args_list[0].args, (('Three'),))
        self.assertEqual(mock_print.call_args_list[1].args, (('Five'),))
        self.assertEqual(mock_print.call_args_list[2].args, ((11),))

    def test_convert__throw_if_not_all_multiple(self):
        '''
        Test that if not a multiple provided, it throws
        an error
        '''
        with self.assertRaises(TypeError) as context:
            Multiple.convert(
                [3,5,6],
                Multiple(3, 'Three'),
                'error'
            )

        self.assertEqual(
            'One argument is not a multiple. All multiple must instance of `Multiple`.',
            str(context.exception)
        )

    def test_convert__skip_any_no_number(self):
        '''
        Test that if no number is provided, skip it.
        This is with the assumption that we don't stop
        the application from working if no number is provided.
        '''
        arr = Multiple.convert(
            [3,'Five',31],
            Multiple(3, 'Three')
        )

        self.assertEqual(arr,['Three','Five',31])

    def test_init(self):
        '''
        Test Constructor
        '''
        p = Multiple(3, 'Three')
        self.assertEqual(p.to_i(), 3)
        self.assertEqual(p.to_s(), 'Three')

    def test_is_in(self):
        '''
        Test logic of is_in
        '''
        p = Multiple(3, 'Three')
        self.assertTrue(p.is_in(9))
        self.assertTrue(p.is_in(27))
        self.assertFalse(p.is_in(22))


if __name__ == '__main__':
    unittest.main()
