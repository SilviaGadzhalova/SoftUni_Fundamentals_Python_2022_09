company_employs = {}
while True:
    current_string = input()
    if current_string == "End":
        break
    current_company, current_id = current_string.split(" -> ")
    if current_company not in company_employs.keys():
        company_employs[current_company] = []
        company_employs[current_company].append(current_id)
    elif current_company in company_employs.keys():
        if current_id not in company_employs[current_company]:
            company_employs[current_company].append(current_id)
for company, employ in company_employs.items():
    print(f"{company}")
    for employ in company_employs[company]:
        print(f"-- {employ}")
