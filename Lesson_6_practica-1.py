students = {
   'Саша': [2,4,6,1,2],
   'Маша': [6,2,1,4,5],
   'Толик': [12,11,10,9,12],
   'Денис': [5,5,0,0,0]
}
average_bal = {}
for id,ball in students.items():
   average_bal[id] = (sum(ball)/len(ball))

maxball = max(average_bal.values())
minball = min(average_bal.values())

print('У него максимальный бал',[x for x,average in average_bal.items() if average == maxball], maxball)
print('У него минимальный бал',[x for x,average in average_bal.items() if average == minball], minball)
