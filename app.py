def new_in_list(my_list, idx, element):
    '''replace in a copy.'''
    if idx  < 0 or idx > (len(my_list) -1):
        return (my_list)

    copy = my_list.copy
    copy[idx] = element
    return copy