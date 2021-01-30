# program, which reads height(feet) of students into a list and convert these heights to cms in a separate list

N= int(input('How many members are there in Class:'))

studentsHeightinfeet=[]
studentsHeightincms=[]

for i in range(N):
    students = float(input("Enter the height of students "))
    studentsHeightinfeet.append(students) #appending all the students height in feet into a list
    L=[float(i)*30.48 for i in studentsHeightinfeet]  #1 feet = 30.48 cms
studentsHeightincms.append(L)  #appending all the student height in cms into a list

print("studentsHeightinfeet : ", studentsHeightinfeet)
print("studentsHeightincms  : ", studentsHeightincms)