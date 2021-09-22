min = 0
max = 10
result = []
exclude = [1,3,4,6,7,88,888,99,999]
for i in range(min, max):
    for j in range(min, max):
        for k in range(min, max):
            for l in range(min, max):
                if i not in exclude and j not in exclude and k not in exclude and l not in exclude:
                    if i != j and j != k and k != l:
                        if int(str(i)+str(j)) not in exclude and int(str(j)+str(k)) not in exclude and int(str(k)+str(l)) not in exclude:
                            if int(str(i)+str(j)+str(k)) not in exclude and int(str(j)+str(k)+str(l)) not in exclude:
                                result.append("{}{}{}{}".format(i, j, k, l))

print("total result: {}".format(len(result)))
print(result)
