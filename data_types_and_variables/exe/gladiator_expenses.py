lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
shield_repairs = 0
for lost in range(1,lost_fights_count+1):
    if lost % 2 ==0:
        total_expenses +=helmet_price
    if lost % 3 ==0:
        total_expenses +=sword_price
    if lost % 6 ==0:
        total_expenses += shield_price
        shield_repairs += 1
    if lost % 12 == 0:
        total_expenses += armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")


# number_of_lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# total_helmets_broken = number_of_lost_fights // 2
# total_swords_broken = number_of_lost_fights // 3
# total_shields_broken = number_of_lost_fights // 6 #number_of_lost_fights // (2+3)
# total_armors_broken = total_shields_broken // 2
# expenses = helmet_price * total_helmets_broken + \
#     sword_price * total_swords_broken + \
#     shield_price * total_shields_broken + \
#     armor_price * total_armors_broken
# print(f"Gladiator expenses: {expenses:.2f} aureus")