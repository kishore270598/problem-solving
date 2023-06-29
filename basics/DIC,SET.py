print('SET')
a=[1,2]
a.append(4)
print(a)
print('DIC')
key1=[]
val=[]
c='A'
d={}
for i in range(0,5,1):
    key1.append(c)
    c=chr(ord(c)+1)
print('key',key1,end='')
print('\n')
for i in range(1,6,1):
    val.append(i)
print('val',val,end='')
print('\n')
for i in range (len(key1)):
    d[key1[i]]=val[i]
print('dic',d)