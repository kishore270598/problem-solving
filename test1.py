import math

num_lines = 4
num_char = num_lines * 2 - 1
for i in range(0, num_lines, 1):
    
    
    count = "A"
    alp = i * 2 + 1
    space = num_char - alp
    #printing left space 
    for k in range(0, space // 2, 1):
        print(" ", end="")
    #printing ascending
    for j in range(0, math.ceil(alp / 2), 1):
        print(count, end="")
        count = chr(ord(count) + 1)
    #printing descedning 
    count= chr(ord(count)-1)
    for o in range (0,math.ceil(alp / 2)-1,1):
        count= chr(ord(count)-1)
        print(count,end='')
    #printing right space
    for l in range(space // 2, 0, -1):
        print(" ", end='')
    print("\n")
