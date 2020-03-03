num = [1, 3, 4, 5, 7, 8, 2, 4]
target = 5

for i in range(0, len(num)):
    # print("i :", num[i])
    for j in range(1, len(num)):
        # print("j :", num[j])
        if target == num[i] + num[j]:
            print(num[i], num[j])
        else:
            pass

