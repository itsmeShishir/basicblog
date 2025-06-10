# for loops 

for i in range(1,11):
    print(i)

# wap to print all the even between 0 to 13
for i in range(0, 14, 2):
    print(i)

for i in range(0, 14):
    if i%2 ==0:
        print(i)

# wap to print multiplication table of 7 (7*0 = 0, 7*10 = 70)
for i in range(0,11):
    print(f'7*{i} = {7*i}')

for i in range(0,71, 7):
    print(i)

# nested loop in python
for i in range(0, 11):
    print(f"table of {i}")
    for j in range(0, 11):
        print(f"{i} *{j} = {i*j}")

for i in range(5, 0, -1):
    for j in range( 1, i+1):
        print(j, end = "")

    print()

for i in range(0, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

# while loop  -> condition, inc/dec, print
i = 0
while i<10:
    i+=1
    print(i)

# break = extis fomr the loop , continue and pass
list1 = [1,2,3,4,5,6,7,8]
for i in list1:
    if 5 == i:
        break
    print(i)

list1 = [1,2,3,4,5,6,7,8]
for i in list1:
    if 5 == i:
        continue
    print(i)

for i in range(0, 10):
    pass

print("helo ")
#wap to print from 10 to 0 using while loop

