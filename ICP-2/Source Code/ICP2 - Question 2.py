#Given a non-negative integernum, return the number of steps to reduce it to zero. 
#If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it

Number = int(input("Enter a positive number "))

def ZeroFunction(Number):
    count = 0
    while Number > 0:
        if Number % 2 == 0:           #checing the number if it is divided by two or not (Even Number) 
            Number = (Number // 2)
            count = count + 1
        else:
            Number = (Number - 1)    #odd number
            count = count + 1
    print("Number of steps to make zero : ", count)

ZeroFunction(Number)