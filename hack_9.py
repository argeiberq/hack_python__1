"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    """Function printing python version."""
    result = [1,2,3]
    return result[0], "@", result[1], "@", result[2], "@" 
r = fn_hack_9()
print(r)