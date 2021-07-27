import time
import functools
import argparse
import os


def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter()-start
        print(
            f"Execution time: {func.__name__} function was {duration}")
        return result
    return wrapper


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input', help='Input String',
                        type=str, required=True)
    return parser.parse_args()


def is_palindrome(input_string):
    """
    Returns a boolean value that represents whether a string is a palindrome or not.
    This function filters out non-alphanumeric characters and ignores spaces.
    These strings will be considered as a palindrome
    '123!!321@@@@',
    'n   ur s e s      r u n   '

    :param input_string: string type input
    :return boolean: True or False
    """

    # Input validations
    if not isinstance(input_string, str):
        raise TypeError('Please input a string')

    # Removes non-alphanumeric characters
    filtered_string = ''.join(filter(str.isalnum, input_string))
    filtered_string = filtered_string.lower()

    # Reverse the filtered string by doing a slice from the end of the string and moving one step back
    # then returns True/False if the reversed and input string is equal
    return filtered_string == filtered_string[::-1]  # O(n)


@ time_decorator
def main():

    args = get_arguments()
    if(is_palindrome(args.input)):
        print(f'{args.input} is a Palindrome!')
    else:
        print(f'{args.input} is not Palindrome!')


if __name__ == '__main__':
    main()
