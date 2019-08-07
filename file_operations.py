
"""
Implement the below file operations.
Close the file after each operation.
"""


def read_file(path):
    with open(path, 'r') as f:
        s = f.read()
    return s
    
    pass


def write_to_file(path, s):
    with open(path, 'w') as f:
        f.write(s)
    
    pass


def append_to_file(path, s):
    with open(path, 'a') as f:
        f.write(s)
    pass


def numbers_and_squares(n, file_path):
    """
    Save the first `n` natural numbers and their squares into a file in the csv format.

    Example file content for `n=3`:

    1,1
    2,4
    3,9
    """

    with open(file_path, 'w') as csv_file:
        
        for i in range(1, n+1):
            st1 = str(i) + ',' + str(i ** 2) + '\n'
            csv_file.write(st1)

           
