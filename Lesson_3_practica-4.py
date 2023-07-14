def banknotes_splitter(money,money_list):
    result_list = []
    for i in money_list:
        count = min(money // i, 10)
        if count > 0:
            result_list.append(f"{count}*{i}")
            money = money - (count * i)
    return " + ".join(result_list)


money = int(input("Enter a number: "))
money_list = [10, 20, 50, 100, 200, 500, 1000]
output = banknotes_splitter(money,money_list)
print(output)