"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    """Function printing python version."""
    result = "fooziman"
    return result.lower()[0:7] + result.upper()[7]

u = fn_hack_4()

print(u)
