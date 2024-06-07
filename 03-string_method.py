 #len is used to count of number of character is used and it is general purpose function

course = 'Pyhton For Beginner'
print(len(course))



# Function are used for general purpose they are not specific to some entity like print and len etc are used for any task
# method are very specific to perfom some task.Not used for general purpose like upper/lower etc used only for string

print(course.upper())
print(course)
print(course.lower())



             # Finding Index of a character or a sequence of character in a string


#Find method is very case specific (lower/upper)

course = 'Pyhton For Beginner'
print( course.find('F') )      
 


                    #Reaplacing a Character OR Sequence of characters.



course = 'Pyhton For Beginner'
print( course.replace('Beginner' , 'Absolute Beginner'))
print(course)


                    # Boolian Expression

#It will print TRUE or FALSE

course = 'Pyhton For Beginner'
print( 'Pyhton' in course )   
