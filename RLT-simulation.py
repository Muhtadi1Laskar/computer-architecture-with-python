"""
    Register Transfer Language is a symbolic notation used to describe
    the flow of data between registers within digital system. 
    RTL is often used to describe the flow of data between register

    a. [20] = 15 This expression states that contents of memory location 20 are equal to number 5
    b. [20] <- 6 States that the number 6 is put into (copied or loaded into) memory location 20
    c. [20] <- [6] Expression indicates that the content of memory location 6 are copied into memory of location 20
    d. [12] <- [3] + 4 Expression indicates that 4 is added to the content of location 4 and stored into the memory location of 12
    e. [19] <- [7] + [8] States that the content of location 7 and 8 are added and saved on the location 19
    f. [4] <- [[2]] This expression states that the pointer [2] is stored inside the location [4]. 

    Python simulation:
    mem[3] <- 3 Load location 3 with 4. Note this RTL not Python
    mem[5] <- 9 Load location 5 with 9
    summation <- mem[3] + mem[4] Add contents of location 3 and 5, and put result in sum
    mem[6] <- sum Store sum in location 6

"""

mem = [0] * 8
mem[3] = 4
mem[5] = 9
summation = mem[3] + mem[5]
mem[6] = summation

print("Memory: ", mem)

"""
    [7, 5, 4, 0, 3, 9, 0, 0]

    [[0]] <- [[1]] + [[2]]
    [[0]] <- [5] + [4] 
    [[0]] <- 9 + 3
    [7] <- 12

    [7, 5, 4, 0, 3, 9, 0, 12]
"""

mem_two = [7, 5, 4, 0, 3, 9, 0, 0]
pointer0 = mem_two[0]
pointer1 = mem_two[1]
pointer2 = mem_two[2]
source1 = mem_two[pointer1]
source2 = mem_two[pointer2]
result = source1 + source2
mem_two[pointer0] = result

print("Memory: ", mem_two)

