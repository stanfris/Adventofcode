list_oxy = []
list_co2 = []
temp = []
bitamount = 12
count0 = 0
count1 = 0
ans1 = 0
ans2 = 0
with open('day_3.txt') as input_file:
    for line in input_file:
        list_oxy.append(line)
    list_co2 = list_oxy

for i in range(bitamount+1):
    if len(list_oxy) > 1:
        for x in range(len(list_oxy)):
            if list_oxy[x][i] == '0':
                count0 += 1
            if list_oxy[x][i] == '1':
                count1 += 1
        if count1 >= count0:
            for x in range(len(list_oxy)):
                if list_oxy[x][i] == '1':
                    temp.append(list_oxy[x])
        else:
            for x in range(len(list_oxy)):
                if list_oxy[x][i] == '0':
                    temp.append(list_oxy[x])
        list_oxy = temp
        temp = []
        count0 = 0
        count1 = 0
    else:
        ans1 = list_oxy[0]
        
    if len(list_co2) > 1:
        for x in range(len(list_co2)):
            if list_co2[x][i] == '0':
                count0 += 1
            if list_co2[x][i] == '1':
                count1 += 1
        if count1 < count0:
            for x in range(len(list_co2)):
                if list_co2[x][i] == '1':
                    temp.append(list_co2[x])
        else:
            for x in range(len(list_co2)):
                if list_co2[x][i] == '0':
                    temp.append(list_co2[x])
        list_co2 = temp
        temp = []
        count0 = 0
        count1 = 0
    else:
        ans2 = list_co2[0]
print(int(ans1, base=2))
print(int(ans2, base=2))
print(int(ans1, base=2) * int(ans2, base=2))