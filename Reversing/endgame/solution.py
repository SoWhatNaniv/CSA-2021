variables = {
    'a' : '',
    'b' : '',
    'c' : '',
    'd' : '',
    'e' : '',
    'f' : ''
}

with open(r"flag", "rb") as file:
    data = file.read()

for i in range(0, 216, 2):

    first_temp = hex(data[i])[2:]
    second_temp = hex(data[i+1])[2:]
    print('Operation:', first_temp, second_temp)

    if first_temp == '1a':
        variables['a'] = second_temp
    if first_temp == '1b':
        variables['b'] = second_temp
    if first_temp == '1c':
        variables['c'] = second_temp
    if first_temp == '1d':
        variables['d'] = second_temp
    if first_temp == '1e':
        variables['e'] = second_temp
    if first_temp == '1f':
        variables['f'] = second_temp

    if first_temp == 'ab':
        variables[second_temp[0]] = str(hex(int(variables[second_temp[0]],16) + int(variables[second_temp[1]], 16))[2:])
    if first_temp == 'ba':
        variables[second_temp[0]] =  str(hex(int(variables[second_temp[0]], 16) - int(variables[second_temp[1]], 16))[2:])
    if first_temp == 'cd':
        variables[second_temp[0]] = str(hex(int(variables[second_temp[0]], 16) * int(variables[second_temp[1]], 16))[2:])
    if first_temp == 'dc':
        variables[second_temp[0]] = str(hex(int(variables[second_temp[0]], 16) // int(variables[second_temp[1]], 16))[2:])

print('-------------FINALE VARIABLES-------------')
print(variables)

print('-------------CONVERTING-------------')
print(bytes.fromhex(variables['a']).decode('utf-8'))