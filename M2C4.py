#Excercise 1:
#List:
students = ['Leyre', 'Manuel', 'Joan', 'Paula']
print(students)

#Tuple:
animals = ('cow', 'horse', 'chicken', 'pig')
print(animals)

#Float:
bill_total = 150.39
print(bill_total)

#Integer:
total_students_id = 420
print(total_students_id)

#Decimal:
from decimal import Decimal
debts_total = Decimal(44.98)
print(debts_total)

#Dictionary:
fourth_grade_class = {
    "1": "Leyre",
    "2": "Manuel",
    "3": "Joan",
    "4": "Paula"
}
print(fourth_grade_class)


#Excercise 2:
import math
bill_total = 150.39
print(math.ceil(bill_total))


#Excercise 3:
# No haría falta volver a importar la biblioteca matemática porque está importada más arriba.
import math
bill_total = 150.39
print(math.sqrt(bill_total))


#Excercise 4:
fourth_grade_class = {
    "1": "Leyre",
    "2": "Manuel",
    "3": "Joan",
    "4": "Paula"
}

first_student_of_fourth_grade_class = fourth_grade_class["1"]
print(first_student_of_fourth_grade_class)


#Excercise 5:
animals = ('cow', 'horse', 'chicken', 'pig')
print(animals[1])


#Excercise 6:
students = ['Leyre', 'Manuel', 'Joan', 'Paula']
students.extend(['Charlie'])
print(students)


#Excercise 7:
""" 
Hago el ejercicio con la lista original, pero podría continuar con 
la del ejercicio anterior y aparecería Charlie como último estudiante.
"""
students = ['Leyre', 'Manuel', 'Joan', 'Paula']
students[0] = 'Valentina'
print(students)


#Excercise 8:
# Vuelvo a realizar el ejercicio con la lista original
students = ['Leyre', 'Manuel', 'Joan', 'Paula']
students.sort()
print(students)


#Excercise 9:
animals = ('cow', 'horse', 'chicken', 'pig')
animals += ('rabbit',)
print(animals)