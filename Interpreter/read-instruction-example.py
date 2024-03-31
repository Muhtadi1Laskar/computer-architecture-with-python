mem = [4, 6, 1, 2, 7, 8, 4, 4, 5]
r = [0, 0, 0, 0, 0, 0, 0, 0]
inst = "add r[4],mem[3],mem[7]"

inst1 = inst.replace(' ', ',')
intst2 = inst1.split(',')
token0 = intst2[0]
token1 = intst2[1]
token2 = intst2[2]
token3 = intst2[3]
value1 = int(token1[2])
value2 = int(token2[4])
value3 = int(token3[4])

if token0 == 'add':
    r[value1] = mem[value2] + mem[value3]

print(f"Register: {r}")