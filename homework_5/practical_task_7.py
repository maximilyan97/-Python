import json
with open('file_for_practical_task_7.txt', 'r', encoding='utf-8') as file, \
        open('file_json_for_practical_task_7.txt', 'w', encoding='utf-8') as file_json:
    count_of_companies_plus = 0
    profit_of_companies_plus = 0
    lst = [dict(), dict()]
    for line in file:
        company = line.split()
        lst[0][company[0]] = int(company[2]) - int(company[3])
        if lst[0][company[0]]:
            count_of_companies_plus += 1
            profit_of_companies_plus += lst[0][company[0]]

        if count_of_companies_plus == 0:
            lst[1]['average_profit'] = 0
        else:
            lst[1]['average_profit'] = profit_of_companies_plus/count_of_companies_plus
    json.dump(lst, file_json)
