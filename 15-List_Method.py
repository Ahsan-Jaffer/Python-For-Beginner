
# these are the operation that we can apply on list

# num = [1,3,4,9,11,19,23,41,10]


                            # APPEND METHOD
# APPEND will add element at end of list.
# If we want to add 20 at end of list then we use append method 


# num = [1,3,4,9,11,19,23,41,10]
# num.append(20)             
# print(num)

                            #INSERT METHOD
# This method will add value in list at index you want to add at.
# If we want to add 15 at index 5        insert(index,value)


# num = [1,3,4,9,11,19,23,41,10]
# num.insert(5,15)
# print(num)

                            #REMOVE METHOD
# it will remove the element. Add that element value.It will remove that element

# num.remove(23)
# print(num)

                            # CLEAR METHOD
#t will clear your list element 

# num.clear()

                            # INDEX METHOD
# finding the index of element

# print(num.index(9)) 

                            #COUNT METHOD
# It print how many time th element is presemt in list

# print(num.count(9))

                            #SORT METHOD

# num.sort()
# print(num)

                            # REVERSE METHOD
# num.reverse()
# print(num)

                            #COPY METHOD
#first list = num   ,     Secnd list = num2

# it will copy first list into second list.If we chnage fisrt list it does not change the second list.
# num2 = num.copy()


                        #Task remove duplicate

numbers = [1,2,1,2,4,5,4,5]
unique = []
# u = set()
for number in numbers:
    # u.add(number)
    if number  not in unique:
        unique.append(number)
                
print(unique)
# print(u)

# ahsan = [1,3,4,2,1,54]
# ahsan.append()
# print(ahsan)
     