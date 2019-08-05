def last_3_characters(x):
    if len(x) < 3:
        return x
    else:
        return x[-3:]
    pass


def first_10_characters(x):
    if len(x) < 10:
        return x
    else:
        return x[:10]
    pass


def chars_4_through_10(x):
    if len(x) < 10:
        return ''
    else:
        return x[4:11]
    pass


def str_length(x):
    return len(x)
    pass


def words(x):
    return x.split()
    pass


def capitalize(x):
    return x.capitalize()
    pass


def to_uppercase(x):
    return x.upper()
    pass
