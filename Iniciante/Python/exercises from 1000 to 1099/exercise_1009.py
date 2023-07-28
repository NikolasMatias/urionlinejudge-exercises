name = str(input())
fixedSalary = float(input())
allSales = float(input())

total = fixedSalary + (allSales*0.15)


print(''.join(['TOTAL = R$ ', "{:.2f}".format(total)]))