# Prime numbers algorithm
import time

t1 = time.time()

primary = []


def if_primary(number):
    for factor in primary:
        if number % factor == 0:
            return False
        if factor * factor > number:
            return True
    return True


def mark_primary(number):
    for i in range(2, number):
        if if_primary(i) is True:
            primary.append(i)
    return


m = 100000000
mark_primary(m)
# print(primary)
print("Amount of prime numbers in range from 2 to", m, ":", (len(primary)))
print("The highest prime number in that range is", (max(primary)))
t2 = time.time()
print("Time of counting:", round(t2 - t1, 2), "sec")
