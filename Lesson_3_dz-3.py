with open("fizz1.txt", "r") as file:
    lines = file.readlines()


fizz, buzz, last = [], [], []


for line in lines:
    values = line.strip().split()
    if len(values) == 3:
        fizz.append(int(values[0]))
        buzz.append(int(values[1]))
        last.append(int(values[2]))


with open("fizz2.txt", "w") as f:
    for i in range(len(fizz)):
        a = int(fizz[i])
        b = int(buzz[i])
        c = int(last[i])
        output = ""
for i in range(1, c + 1):
    if i % b == 0 and i % a == 0:
        output += "FB "
    elif i % a == 0:
        output += "F "
    elif i % b == 0:
        output += "B "
    else:
        output += str(i) + " "
f.write(output.strip() + "\n")
