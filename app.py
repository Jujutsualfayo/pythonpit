def print_reversed_list_integer(my_list=[]):
    '''printing list in reverse. '''
    if isinstance(my_list, list):
        reversed_list = my_list[::-1]
        for i in reversed_list:
            print("{:d}".format(i))
