def add3(a, b, c):
    return sum([a, b, c])


def unpacking1():
    items = [1, 2, 3]
    # Call add3 by passing unpacking items
    return add3(*items)



def unpacking2():
    kwargs = {'a': 1, 'b': 2, 'c': 3}
    # Call add3 by unpacking kwargs
    return add3(**kwargs)


def call_function_using_keyword_arguments_example():
    a = 1
    b = 2
    c = 3
    # Call add3 by passing a, b and c as keyword arguments
    return add3(b=2, a=1, c=3)


def add_n(*args):
    """
    Define `add_n` so that it accepts
    any number of arguments and
    returns the sum of all the arguments
    """
    return(sum(args))
    


def add_kwargs(**kwargs):
    """
    Define `add_kwargs` so that it accepts a and b as keyword arguments
    and returns the sume of these arguments.

    Ensure the function raises an exception when arguments apart from a and b
    are passed to `add_kwargs`
    """
    if ((len(kwargs.keys()) > 2) or (kwargs.keys() != {'a', 'b'})):
        return ('Values other than a and b are entered please correct this issue.')
    else:
        return sum(kwargs.values())
    


def universal_acceptor(*args, **kwargs):
    """
    Define `universal_acceptor` so that it accepts any kind of
    arguments and keyword-arguments,
    and prints the arguments and keyword-arguments.
    """
    print (args)
    print(kwargs)

    

print(unpacking1())
print(unpacking2())
print(call_function_using_keyword_arguments_example())
print(add_n(1,2,3,4,5,6,6,7,))
print(add_kwargs(a=1, b=3))
universal_acceptor(1,2,3, a=1, b=2)