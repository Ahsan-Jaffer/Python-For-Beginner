
# coordinates = (1,2,3)
# suppose
# x cordinate = 1
# y cordinate = 2
# z cordinate = 3
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

#by using unpacking we can do the above procedure with less line of code
# x,y,z = coordinates

# line 13 is identicle to lines 8,9,10 . Both code give same result

coordinates = (1,2,3)
x,y,z = coordinates
print(f"x:{x}\ny:{y}\nz:{z}")
