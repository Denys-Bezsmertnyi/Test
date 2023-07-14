with open("fizz1.txt", "r") as file:
    lines = file.readlines()
    fizz, buzz, last = zip(*(map(int, line.split()) for line in lines if len(line.split()) == 3 ))
    print(fizz,buzz,last)

output = [" ".join(["FB" if not i % b and not i % a else "F" if not i % a else "B" if not i % b else str(i) for i in range(1, c+1)])
          for a,b,c in zip(fizz,buzz,last)
          ]

with open("fizz2.txt","w") as file:
    file.write("\n".join(output))