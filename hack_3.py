"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    """Function printing python version."""
    result = "fooziman"
    return result.upper()[0] + result.lower()[1:8]
#   return result.capital()
u = fn_hack_3()

print(u)