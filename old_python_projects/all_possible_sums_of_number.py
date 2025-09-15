def nest(nomb):
    return nomb

def listlen(numb):
    temp = 0
    lits = []

    for i in range(1, numb+1):
        templist = []
        temp = numb
        temp = temp + 1 - i
        for k in range(1, temp+1):
            if k == temp and temp != 1:
                if k == temp:
                    templist.append(numb - k + 1)
            else:
                templist.append(1)
        lits.append(templist)
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
elif check.lower() == "false":
    output = listlen(inp)
print(output)
