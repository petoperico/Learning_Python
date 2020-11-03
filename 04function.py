"""Function class."""


def hello(name='person', lastname='exposito'):
    """Function that return 'Hello World'.
    name: string,
    lastname: string,

    return: string,
    """
    return f'Hello, {name} {lastname}!'

name = input('Enter your name: ')
string = hello(name)
print(string)
