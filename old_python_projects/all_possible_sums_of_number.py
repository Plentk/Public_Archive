config = {0: [[]], 1: [[1]], 2: [[1,1], [2]]}

def nest(nomb):
    if nomb in config.keys():
        return config[nomb]
    return nomb

def listlen(numb):
    if numb <= 0:
        return []
    if numb == 1:
        return [1]
    temp = 0
    lits = []

    for i in range(2, numb+1):
        print(numb, i)
        templist = [i]
        temp = numb - i
        config_list = nest(temp)
        print(numb, i, config_list)
        for j in config_list:
            j.append(i - temp)
            j.sort()
        print(numb, i, j, config_list)
        lits.extend(config_list)
    return lits


print("Welcome to the making fun of number simulator!")
while True:
    inp = str(input("Input Number to make fun off:\n"))
    if inp.isdigit() == False:
        print("Data Validation Failed\nNumber to make fun of must be Integer.\nYou will be prompted to try again shortly.")
        continue
    inp = int(inp)
    if inp <= 0:
        print("Data Validation Failed\nNumber to make fun of must be a positive integer.\nYou will be prompted to try again shortly.")
        continue
    while True:
        check = input("Input True for all values leading up to number & False to continue program (Program is not case sensitive):\n")
        if check.lower() == "true" or check.lower() == "false":
            break
        print('Data Validation Failed.\nPlease input "True" or "False"\nYou will be prompted to input again shortly.')
    inp = int(inp)
    break
output = []
if check.lower() == "true":
    for j in range(1, inp+1):
        output.append(listlen(j))
        print(j, output[-1])
elif check.lower() == "false":
    output = listlen(inp)
print(output)
