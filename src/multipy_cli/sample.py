#!/usr/bin/env python3

'''
Sample application
'''
# Allow to run in the test context
# and as standalone for demo
# TODO: Find better way to achieve this
if __name__ == '__main__':
  from multiple import Multiple
else:
  from .multiple import Multiple

def main():
    '''
    Main application: looping numbers from 1 to 100 and converting multiples
    of 3 and 5 to string equivalents. If number is multiple of 3 and 5, number
    will be converted to its string equivalent.
    The application will print the result on the console.
    '''
    Multiple.convert(
      range(1, 101),
      lambda value: print(value),
      Multiple(3, 'Three'),
      Multiple(5, 'Five')
    )


if __name__ == '__main__':
    main()