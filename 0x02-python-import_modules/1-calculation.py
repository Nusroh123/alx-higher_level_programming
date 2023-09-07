#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addRes = add(a, b)
    subRes = sub(a, b)
    mulRes = mul(a, b)
    divRes = div(a, b)

    '''
    print("{} + {} = {}".format(a, b, addRes))
    print("{} + {} = {}".format(a, b, subRes))
    print("{} + {} = {}".format(a, b, mulRes))
    print("{} + {} = {}".format(a, b, divRes))
    '''
    '''
    print(a + " + " + b + " = " + addRes)
    print(a + " + " + b + " = " + subRes)
    print(a + " + " + b + " = " + mulRes)
    print(a + " + " + b + " = " + divRes)
    '''
    print(f"{a} + {b} = {addRes}")
    print(f"{a} + {b} = {subRes}")
    print(f"{a} + {b} = {mulRes}")
    print(f"{a} + {b} = {divRes}")
