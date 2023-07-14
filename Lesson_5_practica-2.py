def my_square(num):
    return num**2
def simple_number(num):
    for i in range(2, num):
        if not num % i:
            return False
return True

number_list = list(range(2,51))
result = list(map(my_square, filter(simple_number,number_list)))
print(result)
