import re
def word_count(s):
    """
    Find the number of occurrences of each word
    in a string(Don't consider punctuation characters)
    """
    s = s.replace(",", "")
    s = s.replace(".", "")

    words = s.split()
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
    pass


def dict_items(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    """
    l = [(k,v) for k,v in d.items()]
    return l
    pass


def dict_items_sorted(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    sorted by `d`'s keys
    """
    l = sorted([(k,v) for k,v in d.items()])
    return l
    pass

print(word_count("Python is an interpreted, high-level, general-purpose programming language. Python interpreters are available for many operating systems. Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported."))
