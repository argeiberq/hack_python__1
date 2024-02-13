"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    """Function printing python version."""
    result = "fooziman"

    return result.replace("ooziman", "00z1m@n")
r = fn_hack_5()
print(r)
