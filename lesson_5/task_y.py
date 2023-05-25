s = 'My name is Kyrylo and I study Python'
i = s.find('y')
# print(i)
# print(s.find('y', i + 1))

counter = -1
for word in s:
    for simvol in word:
        counter += 1
        # print(counter, simvol,  simvol.find('y'))
        index = simvol.find('y')
        # print(index)
        if simvol.find('y') != -1:
            print(counter, simvol, index)

