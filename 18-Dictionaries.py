

# Key-Value Pairs
# Elements are enclosed in curly braces{}
# We can change the Element
customer ={
    'Name' : 'Ahsan',
    'Age' : 21,
    "is_verified":True
}
# print(customer)      #whole dictinaries is printed with key and values
# To get one element. Write the key and it return its value.    customer[key_name]
# print(customer["is_verified"])    

                        #GET METHOD
print(customer['Name'])
print(customer.get('Name'))

                        # Updation

# customer['Name'] = "SaqibRasheed"
# print(customer['Name'])

                        #Delete a element
# del customer['Age'] 

# print(customer.values())

# print(customer.keys())


#                   PROJECT

phone = input("Phone: ")

digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
output = ""
for ch in phone :
  output += digit_mapping.get(ch , "!") + " "

print(output)