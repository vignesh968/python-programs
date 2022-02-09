x = "basic language and easy language"


def function():
    global x # x is set to be global so inside & outside of function all take the x value as "best"
    x = "best"
    print("python is " + x)


function()
print(x)