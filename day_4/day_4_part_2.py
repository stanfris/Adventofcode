import time
import copy
linenumber = 0
draws = []
currentfield = []
fields = []
total = 0

with open('day_4.txt') as input_file:
    for line in input_file:
        linenumber += 1
        if linenumber == 1:
            draws = list(map(int, line.split(",")))
        elif (linenumber + 4) % 6 == 0:
            fields.append(currentfield)
            currentfield = []
        else:
            currentfield.append(list(map(int, line.split())))

storage = copy.deepcopy(fields)

for draw in draws:
    amt = len(fields)
    for boardn in range(1, amt):
        for rown in range(5):
            for coln in range(5):
                if fields[boardn][rown][coln] == draw:
                    fields[boardn][rown][coln] = 'x'
    for boardn in range(1, amt):

        for i in range(5):

            if fields[boardn][i][0] == 'x' and fields[boardn][i][1] == 'x' and fields[boardn][i][2] == 'x' and fields[boardn][i][3] == 'x' and fields[boardn][i][4] == 'x':

                print("removing", boardn)
                storage.remove(storage[boardn])
                if len(fields) == 2:
                    for rown in range(5):
                        for coln in range(5):
                            if fields[1][rown][coln] != 'x':
                                total += fields[1][rown][coln]
                    total = total * draw
                    print(total)
                break

            elif fields[boardn][0][i] == 'x' and fields[boardn][1][i] == 'x' and fields[boardn][2][i] == 'x' and fields[boardn][3][i] == 'x' and fields[boardn][4][i] == 'x':

                print("removing", boardn)
                storage.remove(fields[boardn])
                if len(fields) == 2:
                    for rown in range(5):
                        for coln in range(5):
                            if fields[1][rown][coln] != 'x':
                                total += fields[1][rown][coln]
                                print(total)
                    total = total * boardn
                print(total)
                break
