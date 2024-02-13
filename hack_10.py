"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    """Function printing python version."""
    ls2 = []
    result = "fooziman"
    ls2 = list(result.replace("fooziman", "F00Z1M@N"))
    return ls2
r = fn_hack_10()
print(r)
