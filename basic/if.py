# age = 160
# age_alcohol = 20
#
# if age >= age_alcohol:
#     print("You can drink beer!")
# else:
#     print("You are too young to drink beer")
#
# age_drive = 18
# if age >= age_alcohol:
#     print("You can drink beer!")
# elif age < age_drive:
#     print("You cannot even drive!")
# else:
#     print("You are too young to drink beer but you can drive")
#
# print("The value is invalid!")
# if not 0 < age < 120:
#     pass

balance = 80000000
withdraw = 6000000

withdrawal_limit = 1000000

if withdraw > withdrawal_limit:
    print("You cannot drawer")
elif balance > withdraw:
    balance -= withdraw
    print(f"Your new balance is {balance}")
else:
    print("Danger!!")



