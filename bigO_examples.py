def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


print factorial(5)


def permutation(str_, prefix=None):
    if prefix is None:
        return permutation(str_, '')
    if len(str_) == 0:
        print prefix
    else:
        for i in range(len(str_)):
            rem = str_[0:i] + str_[i + 1:]
            permutation(rem, prefix + str_[i])


permutation('123')

def powersOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print 1
        return 1
    else:
        prev = powersOf2(n/2)
        curr = prev * 2
        print curr
        return curr


powersOf2(1024)