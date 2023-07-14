fizz, buzz , last = (int(input()) for i in range(3))
for i in range(1,last+1):
    if i % buzz == 0 and i % fizz == 0: print("FB")
    elif i%fizz ==0: print("F")
    elif i%buzz == 0: print("B")
    else: print(i)
