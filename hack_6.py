"""
loop: for [] output => [0,1,2,3,4,5]
"""
lis = [
    0,1,2,3,4,5
]

def fn_hack_6():
    """Function printing python version."""
    result = []
    for item in lis:
        result.append(item)
    return result


x = fn_hack_6()

print(x)