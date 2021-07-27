
from longest_palindrome import get_longest_palindrome
from palindrome import time_decorator
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input', help='Input String',
                        type=str, required=True)
    return parser.parse_args()


def cut_palindrome(input_string):
    """
    This function returns an integer that represents the minumum number of cuts needed 
    to perform, such that each remaining substring is a palindrome
    :params input_string: string type input
    :return int: number of cuts needed
    """
    # For this approach, I used the existing get_longest_palindrome method.
    # Using that we can identify a palindrome substring from the input and the remaining substring.
    # We have 4 conditions:
    # 1. The input is already a palindrome, No cut needed Return 0
    # 2. The palindrome substring is inbetween 2 substrings.
    #       left_string|[palindrome]|right_string
    #   This means that we need 2 cuts Return + 2.
    # 3. The palindrome substring is on the left.
    #       [palindrome]|right_string
    #   This means that we need 1 cut. Return + 1.
    # 4. The palindrome substring is on the right.
    #       left_string|[palindrome]
    #   This means that we need 1 cut. Return + 1.
    # The next step would be doing a recursion. We would be calling the same method passing
    # all remaining substrings.
    #   Condition 2 - Pass left_string and right_string
    #   Condition 3 and 4 - Pass non empty substring left_string or right_string
    if not isinstance(input_string, str):
        raise TypeError('Please input a string')

    if get_longest_palindrome(input_string) == input_string:
        return 0
    long_str = get_longest_palindrome(input_string)
    left_string = input_string[:input_string.index(long_str)]
    right_string = input_string[(len(long_str)+input_string.index(long_str)):]
    if(left_string and right_string):
        return cut_palindrome(left_string) + cut_palindrome(right_string) + 2
    return cut_palindrome(left_string or right_string) + 1


@time_decorator
def main():

    args = get_arguments()
    print(f'We need {cut_palindrome(args.input)} cuts for {args.input}')


if __name__ == '__main__':
    main()
