import copy


def sum_items_in_list(x):
    return sum(x)
    pass


def list_length(x):
    return len(x)
    pass


def last_three_items(x):
    return x[-3:]
    pass


def first_three_items(x):
    return x[0:3]
    pass


def sort_list(x):
    return sorted(x)
    pass


def append_item(x, item):
    x.append(item)
    return x
    pass


def remove_last_item(x):
    x.pop()
    return x
    pass


def count_occurrences(x, item):
    return x.count(item)
    pass


def is_item_present_in_list(x, item):
    if item in x:
        return True
    else:
        return False
    pass


def append_all_items_of_y_to_x(x, y):
    """
    x and y are lists
    """
    x.extend(y)
    return x
    pass


def list_copy(x):
    """
    Create a shallow copy of x
    """
    return copy.copy(x)
    pass
