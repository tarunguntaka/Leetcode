


doors = [False]*101
for i in range(1,100):
    for j in range(1,101,i):
        doors[j] = not doors[j]


door_n = [i-1 for i in range(len(doors)) if doors[i]==True]
print(door_n)
