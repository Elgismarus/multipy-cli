#!/usr/bin/env python3

'''
Module multiple
'''
import array as arr

class Multiple:
    '''
    Class Multiple represents a number that
    is used to determine whether it is a
    multiple of another number. 
    '''

    @classmethod
    def _process_multiples(cls, multiples, value):
        '''
        Loop through each multiple provided and transform
        to mutliple text value equivalent for each multiple
        matching

        :param  arr multiples   List of Multiple object
        :param  int value       Number to transform
        :return:    Transformed value if any match
        :type:      any
        :TypeError  If any multiple provided is not a Multiple object
        '''
        transformed = value

        for m in multiples:
            if not isinstance(m, Multiple):
                raise TypeError('One argument is not a multiple. All multiple must instance of `Multiple`.')

            transformed = cls._combine(m, value, transformed)

        return transformed

    @classmethod
    def _combine(cls, multiple, original, transformed):
        '''
        Private static class to combine existing multiple previous value
        with new multiple value if required. If no previous multiple and
        number not a multiple of current, just return original value

        :param  Multiple    multiple        Current multiple object to compare against
        :param  int         original        Original number value
        :param  any         transformed     Previous transformed value if previously a multiple of
        :return:    Combine value or original value
        :type: int|str
        '''
        ret = transformed
        converted = (original, multiple.to_s())[multiple.is_in(original)]
        # If both value and converted are integer
        # meaning no conversion happen in past
        # and current. Therefore, keep original
        # value in number
        if type(converted) == str:
            ret = ('', transformed)[type(transformed) == str]
            ret += converted
        return ret

    @classmethod
    def convert(cls, range: arr, after_each: any, *multiples):
        '''
        Analyze a list of multiple numbers, compare them to the range of numbers,
        and convert any number that is a multiple to their multiple string equivalent.
        If a number is a multiple fo many, the string representation is combined.

        The callback is optional. If lambda is supplied, it will be used as a
        callback in each step (number) of the conversion.
        If multiples are provided instead, it will process it as normal multiple.

        :param  arr     range           Array of numbers
        :param  lambda  after_each      (Optional) Callback on each iteration transformed
        :param  tuple   multiples       Multiples objects
        :return: Array of values
        :type: arr
        '''
        ret = []

        # Check if second argument provided is
        # a lambda or Multiple
        # if multiple, include in tuple list
        # to be processed
        if isinstance(after_each, Multiple):
            multiples = (after_each, ) + multiples

        for x in range:
            # All number must be int to
            # be process. Otherwise, skip.
            if not type(x) == int:
                ret.append(x)
                continue

            value = cls._process_multiples(multiples, x)

            if callable(after_each):
                after_each(value)

            ret.append(value)

        return ret

    def __init__(self, number: int, text: str) -> None:
        '''
        Constructor

        :param  int number  The multiple number
        :param  str text    The number text value
        :return: Number object
        '''
        self.number = number
        self.text = text

    def to_i(self):
        '''
        multiple number in integer format

        :return: Number
        :type: int
        '''
        return self.number

    def to_s(self):
        '''
        multiple number in string format
        e.g: 3 => "Three"

        :return: Number in string format
        :type: string
        '''
        return f"{self.text}"

    def is_in(self, number: int):
        '''
        Check if number provided can be
        a multiple

        :param  int number
        :return: boolean
        '''
        return number % self.number == 0
