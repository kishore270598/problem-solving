numberline=5
numberchar=numberline*2
for i in range (1,numberline+1,1):
    #i=0
    #numberstars=2
    #space=8
    #i=1
    #numberstars=4
    #spaces=6
    numberstars=i*2
    space=numberchar-numberstars
    #printing left half of stars
    for j in range (0,numberstars//2,1):
        print('*',end='')
    #printing spaces
    for l in range (0,space,1):
        print(' ',end='')
    #printing right half of stars
    for k in range (0,numberstars//2,1):
        print('*',end='')
    print('\n')
for i in range (0,numberline,1):
    #i=0
    #numberstars=10
    #space=0
    #i=1
    #numberstars=8
    #spaces=2
    space=i*2
    numberstars=numberchar-space
    #printing left half of stars
    for j in range (0,numberstars//2,1):
        print('*',end='')
    #printing spaces
    for l in range (0,space,1):
        print(' ',end='')
    #printing right half of stars
    for k in range (0,numberstars//2,1):
        print('*',end='')
    print('\n')







#numberchar=10
#numberlines=
#star=10