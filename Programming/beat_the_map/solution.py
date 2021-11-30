# First Job
p1 = open(r'C:\Users\niv\Desktop\csa\Programming\beat_the_map\first_hint.bmp', 'rb').read()
p2 = open(r'C:\Users\niv\Desktop\csa\Programming\beat_the_map\second_hint.bmp', 'rb').read()

result = p1[:1078]
for (i, (b,a)) in enumerate(zip(p1[1078:], p2[1078:])):

    if b:
        result += bytes([a])
    else:
        result += bytes([b])

with open(r"C:\Users\niv\Desktop\csa\Programming\beat_the_map\result.bmp", "wb")as fd:
    fd.write(result)

# Second Job
result2=p1[:1078]
for a in p2[1078:]:
    result2 += b'\xff' if a %2 == 0 else b'\x00'

with open(r"C:\Users\niv\Desktop\csa\Programming\beat_the_map\result2.bmp", "wb")as fd:
    fd.write(result2)

# Third Job
p3 = open(r'C:\Users\niv\Desktop\csa\Programming\beat_the_map\challenge.bmp', 'rb').read()
length = len(p3)

# Triangular Series
triangular_series = [0]
for i in range(1, length):
    if triangular_series[-1] + i >= length - 1078:
        break
    triangular_series.append(triangular_series[-1] + i)

# Lsbit Steganography

result3 = list()
for i in triangular_series:
    result3.append(p3[1078 + i] & 0b1)

string = ""
for i in range(0, len(result3), 8):
    string += chr(int("0b" + "".join( str(i) for i in result3[i: i+8] ), 2))

print(string)
