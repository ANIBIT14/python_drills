def integers_from_start_to_end_using_range(start, end, step):
    l = []
    for i in range(start, end, step):
        l.append(i)
    """return a list"""
    return l
    


def integers_from_start_to_end_using_while(start, end, step):
    """return a list"""
    if step > 0:
        l = []
        while (start < end):
            l.append(start)
            start += step
        return l
    if step < 0:
        l = []
        while (start > end):
            l.append(start)
            start += step
        return l
    


def two_digit_primes():
    """
    Return a list of all two-digit-primes
    """
    l = []
    for num in range(10,100):
  
       if num > 1:
            for i in range(2,num):
               if (num % i) == 0:
                   break
            else:
                l.append(num)
    
    return (l)
    

