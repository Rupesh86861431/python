grade=input("enter the grade of employee")
if grade != "A" or grade != "B":
    print("Enter a valid grade , Either A or B")
salary=input("Enter the salary of the employee")
if salary.isalpha():
    print("Enter Integers only")
salary=int(salary)
if int(salary<1):
    print('invalid input')
elif grade=='A':
    if salary < 10000:
        bonus=salary*0.07
    else:
        bonus = salary * 0.05
    print('bonus is',bonus)
    salary = salary + bonus
    print('salary is',salary)
elif grade=='B':
    if salary < 10000:
        bonus=salary*0.12
    else:
        bonus = salary * 0.1
    print("bonus:",bonus)
    salary = salary + bonus
    print("salary is:",salary)

