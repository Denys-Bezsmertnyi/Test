def banknotes_splitter (money,money_list):
    result_list = []
    for i in money_list:
        count = money // i
        if count > 0:
            result_list.append(f'{count} * {i}')
            money = money % i
    return " + ".join(result_list)

money = int(input())
money_list = [1000,500,200,100,50,20,10]
result = banknotes_splitter(money,money_list)
print(result)