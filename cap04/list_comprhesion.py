# squares = [value**2 for value in range(1,11)]
# print(squares)


'''
ant = 0
suc = 1

fibonnaci = [0,1]

print(ant,"\n",suc,"\n")
for fib in range(1,9):
    act = ant + suc
    fibonnaci.append(act)
    ant = suc
    suc = act

print(fibonnaci)
'''

# for n in range(1,21):
#   print(n)


million = [n for n in range(1,101)]
# print("min: ",min(million))
# print("max: ",max(million))
# print(sum(million))

# for i in million:
#  print(i)


impars = [number for number in range(1,21)]

# for i in impars:
#    if(i % 2 != 0):
#        print(i)

multiplos3 = [values*3 for values in range(3,31)]

# for i in multiplos3:
#   print(i)

cubos = [values**3 for values in range(1,11)]

for cubo in cubos:
    print(cubo)