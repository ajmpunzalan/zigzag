from palindrome import is_palindrome, time_decorator
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input', help='Input String',
                        type=str, required=True)
    return parser.parse_args()


def get_longest_palindrome(input_string):
    """
    This function returns the longest palindrome in a given string
    :param input_string: string type input
    :return string: longest palindrome substring 

    This function uses the is_palindrome method. This would inherit the
    behavior of ignoring non-alphanumeric characters.

    """
    if not isinstance(input_string, str):
        raise TypeError('Please input a string')
    # We are searching through the input string using a [window].
    # Initial size would be the length of the input string.
    # We check if the window is a palindrome
    # Return the window if it is a palindrome
    # Else reduce the size of the window by 1
    # Then move the window through the input
    # We do this until we find a palindrome string(Assume there would be 1 longest
    # palindromic substring)
    # Example:
    # input = 'axyzzyxf'
    # [axyzzyxf]
    # [axyzzyx]f
    # a[xyzzyxf]
    # [axyzzy]xf
    # a[xyzzyx]f
    # return [xyzzyx] -> palindrome
    window_size = len(input_string)
    for i in range(window_size):  # O(n)
        start_index = 0
        for end_index in range(window_size-i, window_size+1):  # O(n)
            window_string = input_string[start_index:end_index]
            start_index += 1
            if(is_palindrome(window_string)):
                return window_string


@time_decorator
def main():
    args = get_arguments()
    print(
        f"The longest palindrome in {args.input} is:\n\t'{get_longest_palindrome(args.input)}'")


if __name__ == '__main__':
    main()
