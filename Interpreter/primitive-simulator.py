prog = ['LDRL r0 0','LDRL r1 0','ADDL r1 r1 1','ADD r0 r0 r1','CMPL r1 10','BNE2','STOP']

r = [0] * 8
z = 0
run = True
pc = 0

while run == True:
    inst = prog[pc]
    oldPC = pc
    pc = pc + 1
    inst = inst.split(' ')

    if inst[0] == 'ADD':
        rd = int(inst[1][1])
        rS1 = int(inst[2][1])
        rS2 = int(inst[3][1])
        r[rd] = r[rS1] + r[rS2]

    elif inst[0] == 'ADDL':
        rd = int(inst[1][1])
        rS1 = int(inst[2][1])
        literal = int(inst[3])
        r[rd] = r[rS1] + literal

    elif inst[0] == 'BNE':
        if z == 0:
            pc = int(inst[1])
    
    elif inst[0] == 'CMPL':
        z = 0
        rVal = r[int(inst[1][1])]
        intVal = int(inst[2])
        if rVal == intVal: 
            z = 1
    
    elif inst[0] == 'LDRL':
        rd = int(inst[1][1])
        data = int(inst[2])
        r[rd] = data
    
    elif inst[0] == 'LDRL':
        rd = int(inst[1][1])
        data = int(inst[2])
        r[rd] = data
    
    elif inst[0] == 'STOP':
        run = False
        print("End of program reached")
    
    else:
        run = False
        print('Error turning out')
    
    print('PC = ',oldPC,'r0 = ',r[0],'r1 = ',r[1],'z = ',z)


