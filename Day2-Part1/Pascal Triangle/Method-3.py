# If they want to print the whole row of a given row number

# Time = r
# Space = 1 -> If we try to save in an array then r

r = 10
e_1 = 1
for i in range(1, r+1):
    print(e_1, end=" ")
    e_1 = int(e_1 * (r-i)/i)


    