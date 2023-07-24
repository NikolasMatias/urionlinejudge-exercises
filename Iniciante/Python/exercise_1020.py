dias = int(input())

anos = int(dias/365)
meses = int(dias%365/30)
dias = int(dias%365%30)

print(str(anos)+' ano(s)')
print(str(meses)+' mes(es)')
print(str(dias)+' dia(s)')