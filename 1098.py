
i = 0
j = 1
while i <= 2:
    for a in range(3):
        if int(i) != i:
            print("I={:.1f} J={:.1f}".format(i,j))
        else:

            print("I={:.0f} J={:.0f}".format(i,j))
        j += 1
    i = round(i + 0.2, 1)
    j = round(j - 2.8, 1)