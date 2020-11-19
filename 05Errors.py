"""Error handling class."""
import sys


def windows_validation():
    """Function that generates a Assertion Error."""
    assert ('linux' in sys.platform), "OS Error: This code only run on Windows"
    print('Doing something')

'''def division(int1, int2):
    try:
        return int1/int2
    except:
        raise Exception('Itis not possible the division by zero')

print(division(0,0))'''

try:
    windows_validation()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as file_error:
        print(file_error)
finally:
    print('This is the finally clause')
