studentList = {}
max_students = 45
coach_cost = 550
entry_ticket_cost = 30
student_count = -1

while student_count == -1:
    try:
        student_count = int(input("What is the estimated amount of students coming?\n"))
    except:
        print("Error encountered! Please re-input the number.")
        student_count = -1
    if student_count > max_students:
        print("Too many students! The maximum amount of students allowed is: ", max_students)
        student_count = -1

parking_cost = student_count * 30
rec_ticket_cost = (coach_cost + parking_cost) / student_count
print(f"It will cost you {parking_cost}€ for the parking fee, and {coach_cost + parking_cost}€ in total. \nYou should charge {rec_ticket_cost}€ per student in order to not make a loss.")

pauseChamp = input("Next enter the students who have applied.")
for i in range(1, student_count+1):
    student_name = input(f"What is student #{i}'s name?\n")
    student_hasPaid = 0
    while student_hasPaid not in ["Y","N"]:
        student_hasPaid = input(f"Has the student paid? Y/N\n")
        if student_hasPaid not in ["Y","N"]:
            print("Invalid input. Please enter either Y or N.")
    studentList.update({i:{"id":i,"name":student_name,"paid":student_hasPaid}})
print("Data entry completed!\n")

for i in studentList:
    student = studentList[i]
    student_id = student["id"]
    student_name = student["name"]
    student_paid = student["paid"]
    print(f"#{student_id} || Name: {student_name} || Paid? {student_paid}")

collected_money = -1
while collected_money == -1:
    try:
        collected_money = int(input("How much money have you collected? \n"))
    except:
        print("Invalid input! Please enter a number.")
        collected_money = -1

paid_count = 0
non_paid_count = 0
for i in studentList:
    if studentList[i]["paid"] == "Y":
        paid_count += 1
    else:
        non_paid_count += 1

parking_cost = paid_count * 30
rec_ticket_cost = (coach_cost + parking_cost) / paid_count
print(f"In total, {paid_count} students paid, and {non_paid_count} students did not pay. \nThe cost of the trip is {coach_cost + parking cost}")