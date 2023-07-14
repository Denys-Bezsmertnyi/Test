a = list(range(10)) #0 - 9
sum_of_numbers = 0
for i in a:
    sum_of_numbers += i
sum_of_numbers = 0
dlina = len(a)
shetchik = 0
while shetchik < dlina:
    sum_of_numbers += a[shetchik]
    shetchik +=1
print(sum_of_numbers)
