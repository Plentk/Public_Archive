iterable = "mystring"
"""loops through each character in string iterable"""
for iteration in iterable:
    """condition to check if the iterable has reached i"""
    condition = iteration == "i"
    """If i isn't reached there is no action, just print the character"""
    if not condition:
        print(f"{iteration} - condition not met")
        continue
        print("This code not executed")
    else:
        print("condition met")
        break
        print("This code not executed")