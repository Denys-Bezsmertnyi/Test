with open("fizz1.txt", "r") as file:
    lines = file.readline().split()
a = {}
for line in lines:
    count = lines.count(line)
    a[line] = count
print(sorted(a))
