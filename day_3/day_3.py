count0 = 0
count1 = 1
total = 0

for i in range(12):
    with open('day_3.txt') as input_file:
        for line in input_file:
            if line[i] == '0':
                count0 += 1
            if line[i] == '1':
                count1 += 1
        if count1 > count0:
            total += 2 ** (11-i)
        count0 = 0
        count1 = 1
print((4095-total)*total)

        
            

