students = {
   'Саша': ['Python', 'FrontEnd'],
   'Маша': ['FullStack', 'Java'],
   'Толик': ['Python'],
   'Денис': ['FrontEnd'],
   'Максим': ['FullStack'],
   'Вова': ['Python', 'Java'],
   'Диана': ['Python', 'FrontEnd'],
   'Коля': ['FrontEnd'],

}

print('Они учатся в 2 и более группах',[x for x,group in students.items() if len(group)>=2])
print('Они не учатся на фронтенде',[x for x,group in students.items() if 'FrontEnd' not in group])
print('Они учат или питон или джаву',[x for x,group in students.items() if 'Python' in group or 'Java' in group])