grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Johnny=sum(grades[0])/len(grades[0])
Bilbo=sum(grades[1])/len(grades[1])
Aaron=sum(grades[2])/len(grades[2])
Khendrik=sum(grades[3])/len(grades[3])
Steve=sum(grades[4])/len(grades[4])
Dict=list(students)
Dict.sort()
output={Dict[0]:Aaron,Dict[1]:Bilbo,Dict[2]:Johnny,Dict[3]:Khendrik,Dict[4]:Steve}
print(output)