def isPalindrome(x):
    x = str(x)
    forward = [i for i in x.split()[0]]
    backward = []
    for i in range(len(forward)):
        backward.append(forward[-1 * (i + 1)])
    
    if forward == backward:
        return True
    else:
        return False
    
print(isPalindrome(121))
