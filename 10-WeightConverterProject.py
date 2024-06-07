

weight = int( input("Weight : "))
unit = input("(L)bs or (K)g : ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are {converted} in kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} in pounds')


# Another method 

# def kg_to_lb(weight):
#     return weight / 0.45 


# def lb_to_kg(weight):
#     return weight * 0.45


# choice = int (input("Press 1 to convert weight KG to POUND. \nPress 2 to convert weight POUNd to KG : \n"))
# if choice == 1 :
#     w = int(input("Enter your Weight in KG : "))
#     print(f"Your weight in Pound  {kg_to_lb(w)}")

# if choice == 2 :
#     w = int(input("Enter your Weight in POUND : "))
#     print(f"Your weight in KG : {lb_to_kg(w)}")

