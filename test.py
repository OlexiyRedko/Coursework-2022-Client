import math
factorial = 74
answ = 1
for i in range(factorial):
    answ *= i+1
print(answ)
# given = C7499F01401D6035065DC8F80000000000000000h
# for i in range(len(given)):
#     int(given[i])*math.pow(16, len(given)-i-1)
# print(1137730969072405437263399994670779931855700361216)
print(hex(answ))

answ2 = answ*answ

print(answ2)

print(hex(answ2))
