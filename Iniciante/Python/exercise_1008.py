employeeId = int(input())
hoursWorked = int(input())
cashPerHour = float(input())

salary = hoursWorked * cashPerHour

print(''.join(['NUMBER = ', str(employeeId)]))
print(''.join(['SALARY = U$ ', "{:.2f}".format(salary)]))