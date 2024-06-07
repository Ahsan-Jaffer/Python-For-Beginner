# is_hot = False
# if is_hot:
#     print("Its a Hot day You should take plenty of water")
# else:
#     print("It is Cold Day")
# print("Enjoy your day")

price = 100000
good_credit = input("Do you have Good Credit?\n")

if good_credit == "yes":
    down_payment = price * 0.10
    print(f'Down Payment is {down_payment}')
else:
    down_payment = price * 0.20
    print(f'Down Payment is {down_payment}')
