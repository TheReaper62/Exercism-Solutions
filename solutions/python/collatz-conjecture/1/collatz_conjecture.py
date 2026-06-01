def steps(number):
    steps = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    cur = number
    while cur != 1:
        if cur%2==0:
            cur/=2
        else:
            cur*=3
            cur+=1
        steps += 1
    return steps