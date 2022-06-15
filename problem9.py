from math import sqrt


for i in range(1, 1000):
    for j in range(1, 1000):
        if sqrt(i ** 2 + j **2).is_integer():
            a = i
            b = j
            c = sqrt(a ** 2 + b **2)

            if a + b + c == 1000:
                print(a * b * c)
                break
        