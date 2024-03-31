"""
    Fetch [Mar] <- [PC]        Copy the content of Program Counter to the Memory Address Register
          [PC]  <- [PC] + 1    Increament the counter of Program Counter to point to the address of the next instruction
          [MBR] <- [[Mar]]     Read the instruction from the memory
          [IR]  <- [MBR]       Move the instruction to the the instruction register for processing
          CU    <- [IRopcode]  Transmit the opcode to the control unit
"""



mem = [0] * 16
pc = 0

mem[0] = 0b011000001010
mem[1] = 0b100011111111

def fetch(memory):
    global pc
    mar = pc
    pc = pc + 1
    mbr = memory[mar]
    ir = mbr
    cu = ir >> 8
    address = ir & 0xFF
    return (cu, address)


opCode, address = fetch(mem)
print(f"pc = {pc-1} opcode = {opCode} Oprand = {address}")

opCode, address = fetch(mem)
print(f"pc = {pc-1} opcode = {opCode} Oprand = {address}")

